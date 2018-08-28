#-*- encoding: utf-8 -*-
import os
import pdb
from scipy.spatial import distance
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def test_word(model):
  vec1 = embed_word(model, '특허')
  vec2 = embed_word(model, '출원')
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)

def test_sentence(model):
  vec1 = embed_sentence(model, '사용자가 선택하는 주식 종목에 대한 미래예측 질문을 생성하여 웹서버를 통해 데이터베이스서버로 전달하고 상기 웹서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기')
  vec2 = embed_sentence(model, '관리자가 선정한 업체의 재무성과를 예측해 아를 기반으로 개인 특성 기반의 투자여부를 결정하는 사용자 단말 서비스')
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)


def embed_word(model, word):
  tempfile = "fasttext/tempfile"
  command = "echo " + word + " | ~/fastText-0.1.0/fasttext print-word-vectors " + model + " > " + tempfile
  print command
  os.system(command)
  fp = open(tempfile, 'r')
  line = fp.readline()
  line = line.strip()
  if line == "" or line.find("-nan") >= 0: print "error while embedding"
  vec_tokens = line.split(" ")
  tokens = vec_tokens[-100:]
  vector = []
  for token in tokens:
    vector.append(float(token))
  return vector

def embed_sentence(model, sentence):
  tempfile = "fasttext/tempfile"
  command = "echo " + sentence + " | ~/fastText-0.1.0/fasttext print-sentence-vectors " + model + " > " + tempfile
  print command
  os.system(command)
  fp = open(tempfile, 'r')
  line = fp.readline()
  line = line.strip()
  if line == "" or line.find("-nan") >= 0: print "error while embedding"
  vec_tokens = line.split(" ")
  tokens = vec_tokens[-100:]
  vector = []
  for token in tokens:
    vector.append(float(token))
  return vector

if __name__ == "__main__":
  if len(sys.argv) < 2 or len(sys.argv) > 2:
    print "run with 1 argument for section (abstract, description, claims, sentences)"
    sys.exit()
  model_file = "fasttext/" + sys.argv[1] + ".bin"
  test_word(model_file)
  test_sentence(model_file)
