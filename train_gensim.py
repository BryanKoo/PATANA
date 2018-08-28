#-*- encoding: utf-8 -*-
import os, sys
from gensim.models import FastText
import pdb
reload(sys)
sys.setdefaultencoding('utf-8')

def train(corpus, model_file):
  fp = open(corpus, 'r')
  sentences = []
  while True:
   line = fp.readline()
   if not line:
     break
   line = line.decode('utf-8').strip()
   tokens = line.split(" ")
   sentences.append(tokens)
  fp.close()
  model = FastText(sentences, size=100, window=5, min_count=5, workers=4, sg=1, iter=10, word_ngrams=2)
  model.save(model_file)
  pdb.set_trace()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for patent directory(searched_patents, timed_patents) and section(abstract, description, claims, sentences)"
    sys.exit()
  corpus_file = sys.argv[1] + "/" + sys.argv[2] + "_sbd_words.txt"
  if not os.path.exists(corpus_file):
    print "cannot find " + corpus_file
    sys.exit()
  model_file = "fasttext/" + sys.argv[2] + "_gensim.bin"
  train(corpus_file, model_file)
