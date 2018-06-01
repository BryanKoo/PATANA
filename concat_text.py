#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def concat_texts(file_name):
  first_slash = file_name.find("/")
  patent_type = file_name[:first_slash]

  with open(file_name, "r") as a:
    text = a.read()
  print file_name
  concat = open(patent_type + "/text/concat.txt", "a")
  concat.write(text)
  concat.close()

if __name__ == "__main__":
  text_dir = "searched_patents/text/"
  concat_file = text_dir + "concat.txt"
  if os.path.exists(concat_file):
    os.remove(concat_file)
  files = os.listdir(text_dir)
  for file in files:
    if file.endswith("txt"):
      concat_texts(text_dir + file)
