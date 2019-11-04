"""
Use imagemagick to convert all pfds to a sequence of thumbnail images
requires: sudo apt-get install imagemagick
On my mac: `brew install imagemagick`
BASED ON ANDREJ KARPATHY'S SCRIPT https://github.com/karpathy/arxiv-sanity-preserver/blob/master/thumb_pdf.py
but added in my personal `ref` stuff https://github.com/jzbontar/ref
So this is stuck on python2 until we update ref.
"""

import os
import time
import shutil
import subprocess

import ref; ref.init()

import arxiv

## refname, arxivid, selected
# NOTE todo sometime? add openreview id's instead of just arxiv
# sercu2019interactive, Hkl8EILFdN, false
publist = """
mroueh2019sobolev, 1910.14212, false
sercu2019interactive, , true
sercu2019multi, 1907.13121, false
dognin2019wasserstein, 1902.04999, false
das2018pepcvae, 1810.07743, false
chen2018big, 1807.03848, false
mroueh2018sobolev, 1805.12062, true
dognin2018improved, 1805.00063, false
sercu2017semi, 1712.02505, true
mroueh2017sobolev, 1711.04894, false
saon2017english, 1703.02136, false
sercu2017network, , false
mroueh2017fisher, 1705.09675, false
mroueh2017mcgan, 1702.08398, false
sercu2016dense, 1611.09288, true
sercu2016advances, 1604.01792, false
saon2016ibm, 1604.08242, false
sercu2015very, 1509.08967, true
"""
publist = [ [x.strip() for x in entry.split(',')] for entry in publist.strip().split('\n')]
pub_dates_manual = { # default: get them from arXiv
    'sercu2017network': '2017-03-05',
    'sercu2019interactive': '2019-03-27',
}
inpdir = '/Users/tsercu/Dropbox/ref/documents'
outdir = 'assets/paper_thumbs'
tmpdir = os.path.join(outdir,'tmp')
yamldir = '_posts/pubs'
# create if necessary the directories we're using for processing and output
if not os.path.exists(outdir): os.makedirs(outdir)
if not os.path.exists(tmpdir): os.makedirs(tmpdir)
if not os.path.exists(yamldir): os.makedirs(yamldir)


headers = 'author', 'title', 'year', 'filename', 'bibtex'
yaml_template =  """---
title: "{}"
author: "{}"
journal: "{}"
year: {}
arxiv: "{}"
shortname: {}
thumbnail: /{}/{}.png
excerpt: ""
abstract: >
{}
selected: {}
category: pubs
---
"""

#arxivlist = arxiv.query(search_query="sercu", max_results=100)
#print '\n'.join(sorted(['%s   %s' % (r['id'][-12:-2], r['title']) for r in res], reverse=True))

#def getrefname(b):
    #i,j = b.index('{'),  b.index(',') 
    #return b[i+1:j]

def query_res(refname):
    query = "SELECT {} from documents WHERE bibtex LIKE '%{}%'".format(','.join(headers), refname)
    refres = list(ref.con.execute(query).next())
    author, title, year, filename, bibtex = refres
    bibdic = ref.parse_bibtex(bibtex)
    author = bibdic['author'] # include firstnames 
    refres[0] = author
    return refres + [bibdic]

def write_yaml_post(refname, arxivid, selected, ref_metadata):
    author, title, year, filename, bibtex, bibdic = ref_metadata
    abstract = ''
    #refname = getrefname(bibtex)
    print(refname)
    if arxivid:
        arxivres = arxiv.query(id_list=[arxivid])[0]
        author = ', '.join(arxivres['authors'])
        abstract = arxivres['summary']
        if not filter(str.isalnum, str(arxivres['title'])).lower() == filter(str.isalnum, title).lower():
            print('WARNING arxiv title "{}" != "{}"'.format(arxivres['title'], title))
        pubdate = arxivres['published'].split('T')[0]
    else:
        pubdate = pub_dates_manual[refname]
    # yaml long strings with gt (>) then indented lines.
    abstract = '\n'.join('    '+li for li in abstract.split('\n'))
    ###### WRITE YAML ALWAYS
    yaml = yaml_template.format(title, author, bibdic['journal'], year, arxivid, refname,
            outdir, refname, abstract, selected)
    with open(os.path.join(yamldir, '{}-{}'.format(pubdate, refname+'.md')),'w') as fh:
        fh.write(yaml)
    #import ipdb; ipdb.set_trace()


def make_thumbnail(refname, arxivid, selected, ref_metadata):
    author, title, year, filename, bibtex, bibdic = ref_metadata
    ####### MAKE THUMBNAIL
    pdf_path = os.path.join(inpdir, filename)
    thumb_path = os.path.join(outdir, refname + '.png')

    if os.path.isfile(thumb_path): 
        print("skipping {}, thumbnail already exists.".format(refname))
        return

    # erase previous intermediate files thumb-*.png in the tmp directory
    f = os.path.join(tmpdir, 'thumb-*.png')
    subprocess.call('rm '+f, shell=True)

    # spawn async. convert can unfortunately enter an infinite loop, have to handle this.
    # this command will generate 8 independent images thumb-0.png ... thumb-7.png of the thumbnails
    cmd = ['convert', '%s[0-7]' % (pdf_path, ), '-thumbnail', 'x300', os.path.join(tmpdir, 'thumb.png')]
    print(cmd)
    pp = subprocess.Popen(cmd)
    t0 = time.time()
    while time.time() - t0 < 20: # give it 15 seconds deadline
        ret = pp.poll()
        if not (ret is None):
            # process terminated
            break
        time.sleep(0.1)
    ret = pp.poll()
    if ret is None:
        print("convert command did not terminate in 20 seconds, terminating.")
        pp.terminate() # give up

    if not os.path.isfile(os.path.join(tmpdir, 'thumb-0.png')):
        # failed to render pdf, replace with missing image
        missing_thumb_path = os.path.join('static', 'missing.png')
        subprocess.call('cp %s %s' % (missing_thumb_path, thumb_path), shell=True)
        print("could not render pdf, creating a missing image placeholder")
    else:
        cmd = "montage -mode concatenate -quality 80 -tile x1 %s %s" % (os.path.join(tmpdir, 'thumb-*.png'), thumb_path)
        print(cmd)
        subprocess.call(cmd, shell=True)

    time.sleep(0.01) # silly way for allowing for ctrl+c termination

## CHECK IF ANY ARE MISSED
arxivlist = arxiv.query(query="sercu", max_results=100)
# hah got a pretty unique last name, first of my name to publish on arxiv
arxivset  = set([r['id'][-12:-2] for r in arxivlist])
pubset    = set([x[1] for x in publist if x[1]])
notcovered = arxivset - pubset
if notcovered:
    print('WARNING!!! THESE IDS ON ARXIV ARE NOT USED')
    print(notcovered)

for refname, arxivid, selected in publist:
    ref_metadata = query_res(refname)
    write_yaml_post(refname, arxivid, selected, ref_metadata)
    make_thumbnail(refname, arxivid, selected, ref_metadata)
