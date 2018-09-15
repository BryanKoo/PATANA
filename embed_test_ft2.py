#-*- encoding: utf-8 -*-
import os, sys
import fastText
import pdb
from scipy.spatial import distance
from sbd_text import remove_stopword
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
  if len(sys.argv) < 2 or len(sys.argv) > 2:
    print "run with 1 arguments for section(abstract, description, claims, sentences)"
    sys.exit()
  model_file = "fasttext/" + sys.argv[1] + "_pyft.bin"

  w2v = fastText.load_model(model_file)
  vec1 = w2v.get_word_vector(u'특허')
  vec2 = w2v.get_word_vector(u'출원')
  #print distance.cosine(vec1, vec2)
  #print distance.euclidean(vec1, vec2)

  str1 = u'사용자가 선택하는 주식 종목에 대한 미래예측 질문을 생성하여 웹서버를 통해 데이터베이스서버로 전달하고 상기 웹서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기'
  str2 = u'관리자가 선정한 업체의 재무성과를 예측해 아를 기반으로 개인 특성 기반의 투자여부를 결정하는 사용자 단말 서비스'
  str1 = remove_stopword(str1)
  str2 = remove_stopword(str2)
  vec1 = w2v.get_sentence_vector(str1)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u''
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
