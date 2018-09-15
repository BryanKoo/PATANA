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
  str1 = remove_stopword(str1)
  vec1 = w2v.get_sentence_vector(str1)

  str2 = u'고객이 선택하는 증권 종목에 대한 미래예측 질문을 생성하여 웹서버를 통해 데이터베이스서버로 전달하고 상기 웹서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 고객 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  pdb.set_trace()
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'사용자가 선택하는 주식 종목에 대한 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'고객이 선택하는 증권 종목에 대한 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 고객 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'사용자가 선택하는 주식 종목에 대한 미래예측 질문을 생성하여 서버로 전달하고 상기 서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'고객이 선택하는 증권 종목에 대한 미래예측 질문을 생성하여 서버로 전달하고 상기 서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 고객 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'투자결정을 위한 규칙기반정보를 수신하는 고객 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'사용자가 선택하는 주식 종목에 대한 미래예측 질문을 생성하는 사용자 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'고객이 선택하는 증권 종목에 대한 미래예측 질문을 생성하는 고객 단말기'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'주식 종목에 대한 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 생성하는 서버'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'증권 종목에 대한 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 생성하는 서버'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'주식 종목에 대한 미래예측 질문에 대응하는 규칙기반정보를 생성하는 서버'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'증권 종목에 대한 미래예측 질문에 대응하는 규칙기반정보를 생성하는 서버'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
  print ""

  str2 = u'사용자가 선택하는 주식 종목에 대한 미래예측 질문을 생성하여 웹서버를 통해 데이터베이스서버로 전달하고 상기 웹서버로부터 상기 미래예측 질문에 대응하는 투자결정을 위한 규칙기반정보를 수신하는 사용자 단말기로 구성되며  다음의 수학식 1을 기반으로 미래의 특정 시점에 대한 상기 분석대상기업의 기본 예상 주식 가치를 산출하는 기본예상가치산출부 및, 다음의 수학식 2를 기반으로 미래의 특정 시점에 대한 상기 분석대상기업의 재투자비율 활용 주식 가치를 산출하는 재투자적정가치산출부를 포함하는 가치산출모듈;을 포함하는 것을 특징으로 하는, 재무제표 분석을 통한 주식 가치 예측 시스템.'
  str2 = remove_stopword(str2)
  vec2 = w2v.get_sentence_vector(str2)
  print str2
  print distance.cosine(vec1, vec2)
  print distance.euclidean(vec1, vec2)
