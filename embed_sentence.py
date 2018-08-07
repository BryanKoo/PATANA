#-*- encoding: utf-8 -*-
import os
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def embed_sentences(filename):
  vec_filename = filename[:-3] + "vec"
  if not os.path.exists(vec_filename):
    command = "~/fastText/fasttext print-sentence-vectors ~/patana/fasttext/all.bin < " + filename + " > " + vec_filename
    print command
    os.system(command)
  os.remove(filename)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for patent directory(searched_patents, timed_patents) and type of extraction(abstract, description, claims, sentences)"
    sys.exit()
  text_dir = sys.argv[1] + "/" + sys.argv[2] + "/"
  files = os.listdir(text_dir)
  if len(files) < 1:
    print "wrong patent directory: " + text_dir
    sys.exit()
  for file in files:
    if file.endswith("words.txt"):
      embed_sentences(text_dir + file)
