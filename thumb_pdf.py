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
import datetime

import ref; ref.init()

xinfo = """
"""

inpdir = '/Users/tomsercu/Dropbox/ref/documents'
outdir = 'assets/paper_thumbs'
tmpdir = os.path.join(outdir,'tmp')
yamldir = '_posts/pubs'
# create if necessary the directories we're using for processing and output
if not os.path.exists(outdir): os.makedirs(outdir)
if not os.path.exists(tmpdir): os.makedirs(tmpdir)
if not os.path.exists(yamldir): os.makedirs(yamldir)


headers = 'docid', 'author', 'title', 'year', 'filename', 'bibtex'
for field, docs in ref.search_documents(headers, 'sercu'):
    if field == 'author': # search author == sercu.
        break

#TODO
#import arxiv
#res=arxiv.query(search_query="sercu", max_results=100)

def getrefname(b):
    i,j = b.index('{'),  b.index(',') 
    return b[i+1:j]
for doc in docs:
    docid, author, title, year, filename, bibtex = doc
    bibdic = ref.parse_bibtex(bibtex)
    print filename
    print bibdic
    #print bibtex[:100]
    refname = getrefname(bibtex)
    print refname
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
category: pubs
---
"""
    yaml = yaml.format(title, author, bibdic['journal'], year, bibdic['eprint'], refname,
            outdir, refname)
    yamldate = datetime.date(year, 1, 1)
    with open(os.path.join(yamldir, '{}-{}'.format(str(yamldate), refname+'.md')),'w') as fh:
        fh.write(yaml)
    #import ipdb; ipdb.set_trace()


    ####### MAKE THUMBNAIL
    pdf_path = os.path.join(inpdir, filename)
    thumb_path = os.path.join(outdir, refname + '.png')

    if os.path.isfile(thumb_path): 
        print("skipping %s, thumbnail already exists." % (pdf_path, ))
        continue

    # erase previous intermediate files thumb-*.png in the tmp directory
    f = os.path.join(tmpdir, 'thumb-*.png')
    subprocess.call('rm '+f, shell=True)

    # spawn async. convert can unfortunately enter an infinite loop, have to handle this.
    # this command will generate 8 independent images thumb-0.png ... thumb-7.png of the thumbnails
    pp = subprocess.Popen(['convert', '%s[0-7]' % (pdf_path, ), '-thumbnail', 'x156', os.path.join(tmpdir, 'thumb.png')])
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
        cmd = "montage -mode concatenate -quality 80 -font Arial -tile x1 %s %s" % (os.path.join(tmpdir, 'thumb-*.png'), thumb_path)
        print(cmd)
        subprocess.call(cmd, shell=True)

    time.sleep(0.01) # silly way for allowing for ctrl+c termination
