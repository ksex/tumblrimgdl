"""
tumblrimgdl.py

Downloads images from a specific tumblr paged on a range of pages

Usage: python tumblrimgdl.py http://example.com [start page defaults 1] [end page defaults 2] [output directory relative to path]

"""

from bs4 import BeautifulSoup as bs
import urlparse
import random
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

def main(url, out_folder, start_page, end_page):
   
    for x in range(start_page, end_page + 1):
        url2 = url + '/page/' + str(x)
        print url2
        soup = bs(urlopen(url2))
        parsed = list(urlparse.urlparse(url2))

        for image in soup.findAll("img"):
            image_url = urlparse.urljoin(url, image['src'])
            if not "impixu?" in image_url and not "quantserve" in image_url: 
                print "Image: %(src)s" % image

                filename = image["src"].split("/")[-1]
                filename = filename[:75]
                outpath = os.path.join(out_folder, filename)
                urlretrieve(image_url, outpath)


def _usage():
    print "python tumblrimgdl.py http://example.com [start page defaults 1] [end page defaults 2] [output directory relative to path]"

if __name__ == "__main__":
    url = sys.argv[1]
    folder = sys.argv[2]
    
    start = 1
    if sys.argv[3:]:
        start = int(sys.argv[3])
    
    end = 2
    if sys.argv[4:]:
        end = int(sys.argv[4])

    if not url.lower().startswith("http"):
        if not url.lower().startswith("http"):
            _usage()
            sys.exit(-1)
    main(url, folder, start, end)
