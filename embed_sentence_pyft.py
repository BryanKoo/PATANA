#-*- encoding: utf-8 -*-
import os
import fasttext
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
  if os.path.exists(vec_filename):
    os.remove(filename)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "run with 2 arguments for subdir (searched_patents, timed_patents) and section (abstract, description, claims, sentences)"
    print "or run with 1 arguments for subdir (searched_patents, timed_patents) and section (abstract, description, claims, sentences)"
    sys.exit()
  elif len(sys.argv) == 2:
    if not os.path.exists(sys.argv[1]):
      print "cannot find file " + sys.argv[1]
      sys.exit()
    embed_sentences(sys.argv[1])
  elif len(sys.argv) == 3:
    sub_dir = sys.argv[1]
    if sub_dir[-1] == "/":
      sub_dir = sub_dir[:-1]
    text_dir = sub_dir + "/" + sys.argv[2] + "/"
    files = os.listdir(text_dir)
    if len(files) < 1:
      print "wrong patent directory: " + text_dir
      sys.exit()
    for file in files:
      if file.endswith("words.txt"):
        embed_sentences(text_dir + file)
