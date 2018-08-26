#-*- encoding: utf-8 -*-
import os, sys
import fasttext
import pdb
from scipy.spatial import distance
reload(sys)
sys.setdefaultencoding('utf-8')

def train(corpus, model):
  model = fasttext.skipgram(corpus, model, dim=100, epoch=50, bucket=200000, word_ngrams=2)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for patent directory(searched_patents, timed_patents) and type of extraction(abstract, description, claims, sentences)"
    sys.exit()
  corpus_file = sys.argv[1] + "/" + sys.argv[2] + "_sbd_words.txt"
  if not os.path.exists(corpus_file):
    print "cannot find " + corpus_file
    sys.exit()
  model_file = sys.argv[2]
  train(corpus_file, model_file)
