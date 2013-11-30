"""
tumblrimgdl.py

Downloads images from a specific tumblr paged on a range of pages

Usage: python tumblrimgdl.py http://example.com [output directory relative to path] [start page defaults 1] [end page defaults 2] 

"""

from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
import argparse

class Tumblrimgdl(object):
  def __init__(self):
    parser = argparse.ArgumentParser(description='Download all images from a specific tumblr url.')
    parser.add_argument('tumblr_url', metavar='u', type=str,
               help='tumblr url (eg http://fake.tumblr.com)') 
    parser.add_argument('output_folder', metavar='o', type=str,
               help='source folder (relative to current path)')    
    parser.add_argument('start_page', metavar='s', type=int,
               help='Start page (defaults to 1)', default='1')
    parser.add_argument('end_page', metavar='e', type=int,
               help='End page (defaults to 2)', default='2')

    self.args = parser.parse_args()
    self.base_url = os.getcwd()

  def dl_imgs(self):
    self.parse_imgs(self.args.tumblr_url, self.args.output_folder, self.args.start_page, self.args.end_page)

  def parse_imgs(self, tumblr_url, output_folder, start_page, end_page):
     
    for x in range(start_page, end_page + 1):
      url2 = tumblr_url + '/page/' + str(x)
      soup = bs(urlopen(url2))
      parsed = list(urlparse.urlparse(url2))

      for image in soup.findAll("img"):
        image_url = urlparse.urljoin(tumblr_url, image['src'])
        if not "impixu?" in image_url and not "quantserve" in image_url: 
          print "Image: %(src)s" % image

          filename = image["src"].split("/")[-1]
          filename = filename[:75]
          out = os.path.join(self.base_url, output_folder)
          outpath = os.path.join(out, filename)
          urlretrieve(image_url, outpath)


if __name__ == '__main__':
  tumblrimgdl = Tumblrimgdl()
  tumblrimgdl.dl_imgs()
