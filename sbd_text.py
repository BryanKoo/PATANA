#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
sys.path.append("/home/khkoo/crawl/mt-crawlers")
from utils.lang_util import has_hanja, has_hangul, has_alpha
from utils.sentence_segmenter_en import sentence_segmenter
reload(sys)
sys.setdefaultencoding('utf-8')

def sbd_text():
  fin = open("searched_patents/text/concat.txt", "r")
  fout = open("searched_patents/text/concat_sbd.txt", "w")
  while True:
    line = fin.readline().decode("utf-8")
    if not line: break
    line = line.strip()
    if line == "": continue
    if not has_hangul(line): continue
    lines = sentence_segmenter(line, "ko")
    for line in lines:
      fout.write(line + "\n")

if __name__ == "__main__":
  sbd_text()
