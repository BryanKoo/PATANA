#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def concat_texts(file_name, ex_type):
  first_slash = file_name.find("/")
  patent_type = file_name[:first_slash]

  with open(file_name, "r") as a:
    text = a.read()
  print file_name
  concat = open(patent_type + "/" + ex_type + ".txt", "a")
  concat.write(text)
  concat.close()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for patent directory(searched_patents, timed_patents) and type of extraction(abstract, description, claims, sentences)"
    sys.exit()
  text_dir = sys.argv[1] + "/" + sys.argv[2] + "/"
  files = os.listdir(text_dir)
  if len(files) < 1:
    print "wrong patent directory: " + text_dir
    sys.exit()
  concat_file = sys.argv[1] + "/" + sys.argv[2] + ".txt"
  if os.path.exists(concat_file):
    os.remove(concat_file)
  for file in files:
    if file.endswith("txt"):
      concat_texts(text_dir + file, sys.argv[2])
