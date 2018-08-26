#-*- encoding: utf-8 -*-
import os, sys
import fasttext
import pdb
from scipy.spatial import distance
reload(sys)
sys.setdefaultencoding('utf-8')

def test(model):
  w2v = fasttext.load_model(model)
  vec1 = w2v['특허']
  vec2 = w2v['발명']
  vec3 = w2v['발명 특허']
  vec4 = w2v['특허 발명']
  print distance.cosine(vec1, vec2)
  print distance.cosine(vec1, vec3)
  print distance.cosine(vec1, vec4)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "run with 1 arguments for type of extraction(abstract, description, claims, sentences)"
    sys.exit()
  model_file = sys.argv[1] + ".bin"
  test(model_file)
