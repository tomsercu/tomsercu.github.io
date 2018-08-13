"""
Use imagemagick to convert all pfds to a sequence of thumbnail images
requires: sudo apt-get install imagemagick
BASED ON ANDREJ KARPATHY'S SCRIPT https://github.com/karpathy/arxiv-sanity-preserver/blob/master/thumb_pdf.py
but added in my personal `ref` stuff https://github.com/jzbontar/ref
"""

import os
import time
import shutil
import subprocess

import ref; ref.init()

publist = """
chen2018big, 1807.03848, false
mroueh2018regularized, 1805.12062, false
dognin2018improved, 1805.00063, false
sercu2017semi, 1712.02505, true
mroueh2017sobolev, 1711.04894, false
saon2017english, 1703.02136, false
sercu2017network, , false
mroueh2017fisher, 1705.09675, true
mroueh2017mcgan, 1702.08398, false
sercu2016dense, 1611.09288, true
sercu2016advances, 1604.01792, false
saon2016ibm, 1604.08242, false
sercu2015very, 1509.08967, true
"""
publist = [ [x.strip() for x in entry.split(',')] for entry in publist.strip().split('\n')]

inpdir = '/Users/tomsercu/Dropbox/ref/documents'
outdir = 'assets/paper_thumbs'
tmpdir = os.path.join(outdir,'tmp')
yamldir = '_posts/pubs'
# create if necessary the directories we're using for processing and output
if not os.path.exists(outdir): os.makedirs(outdir)
if not os.path.exists(tmpdir): os.makedirs(tmpdir)
if not os.path.exists(yamldir): os.makedirs(yamldir)


headers = 'author', 'title', 'year', 'filename', 'bibtex'

import arxiv
#arxivlist = arxiv.query(search_query="sercu", max_results=100)
#print '\n'.join(sorted(['%s   %s' % (r['id'][-12:-2], r['title']) for r in res], reverse=True))

#def getrefname(b):
    #i,j = b.index('{'),  b.index(',') 
    #return b[i+1:j]

for refname, arxivid, selected in publist:
    query = "SELECT {} from documents WHERE bibtex LIKE '%{}%'".format(','.join(headers), refname)
    refres = list(ref.con.execute(query).next())
    author, title, year, filename, bibtex = refres
    bibdic = ref.parse_bibtex(bibtex)
    author = bibdic['author'] # include firstnames 
    abstract = ''
    #refname = getrefname(bibtex)
    print refname
    if arxivid:
        arxivres = arxiv.query(id_list=[arxivid])[0]
        author = ', '.join(arxivres['authors'])
        abstract = arxivres['summary']
        assert filter(str.isalnum, str(arxivres['title'])).lower() == filter(str.isalnum, title).lower()
    ###### WRITE YAML ALWAYS
    yaml =  """---
title: "{}"
author: "{}"
journal: "{}"
year: {}
arxiv: "{}"
shortname: {}
thumbnail: /{}/{}.png
excerpt: ""
abstract: "{}"
selected: {}
category: pubs
---
"""
    yaml = yaml.format(title, author, bibdic['journal'], year, arxivid, refname,
            outdir, refname, abstract, selected)
    yamldate = arxivres['published'].split('T')[0]
    with open(os.path.join(yamldir, '{}-{}'.format(yamldate, refname+'.md')),'w') as fh:
        fh.write(yaml)
    #import ipdb; ipdb.set_trace()


    ####### MAKE THUMBNAIL
    pdf_path = os.path.join(inpdir, filename)
    thumb_path = os.path.join(outdir, refname + '.png')

    if os.path.isfile(thumb_path): 
        #print("skipping %s, thumbnail already exists." % (pdf_path, ))
        continue

    # erase previous intermediate files thumb-*.png in the tmp directory
    f = os.path.join(tmpdir, 'thumb-*.png')
    subprocess.call('rm '+f, shell=True)

    # spawn async. convert can unfortunately enter an infinite loop, have to handle this.
    # this command will generate 8 independent images thumb-0.png ... thumb-7.png of the thumbnails
    pp = subprocess.Popen(['convert', '%s[0-7]' % (pdf_path, ), '-thumbnail', 'x300', os.path.join(tmpdir, 'thumb.png')])
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
arxivlist = arxiv.query(search_query="sercu", max_results=100)
# query may need to be more specific if your last name is wang.
arxivset  = set([r['id'][-12:-2] for r in arxivlist])
pubset    = set([x[1] for x in publist if x[1]])
notcovered = arxivset - pubset
if notcovered:
    print('WARNING!!! THESE IDS ON ARXIV ARE NOT USED')
    print(notcovered)
