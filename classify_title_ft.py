#-*- encoding: utf-8 -*-
import os, sys
import datetime
import fasttext
import pdb
sys.path.append("..")
from tokenizer.filter_tokenize import tokenize_refine, tokenize_mecab
sys.setdefaultencoding('utf-8')
reload(sys)

classifier = fasttext.load_model('../classifier/classify_title.bin')

def classify_title(line):
  refined = tokenize_refine(line)
  if refined == "":
    refined = line
  title = " ".join(refined)
  title = tokenize_mecab(title)
  if title == "": return ["NA"]
  texts = [title]
  results = classifier.predict_proba(texts, 1)
  categories = []
  for result in results[0]:
    category = result[0][9:]
    probability = result[1]
    if probability > 0.2:
      categories.append(category)
  return categories

def compare_category(title1, title2):
  cats1 = classify_title(title1)
  #print title1, cats1[0]
  cats2 = classify_title(title2)
  #print title2, cats2[0]
  if "NA" in cats1 or "NA" in cats2: return False
  for cat1 in cats1:
    for cat2 in cats2:
      if cat1 == cat2 or get_upper(cat1) == get_upper(cat2):
        return True
  return False

def get_upper(category):
  uppers = {
    u'브랜드 여성의류': u'브랜드패션',
    u'주방가전': u'가전',
    u'이미용가전': u'가전',
  }
  if category in uppers:
    return uppers[category]
  else:
    return category

def train():
  classifier = fasttext.supervised('train80ft_mecab.txt', 'classify_title', dim=100, epoch=50, bucket=200000, word_ngrams=2)

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "train":
    train()
    titles = []
  elif len(sys.argv) > 1:
    titles = [sys.argv[1]]
  else:
    titles = [
      u'[핫트랙스] 테드 브라운 - SHADES OF BROWN',
      u'[CJ]제일제당 H.O.P.E 팻다운톡 10포2세트 (총20포)+디팻 옴므 112정 (4주분)',
      u'[GOO.N] 2015년형 군 밴드 기저귀 3팩!!',
      u'려샴푸 자양윤모 1340ml/린스/한방/함빛/청아/진생보',
      u'브라운 멀티퀵7 핸드블렌더 MQ775 (정품)',
      u'브라운 오랄비 MD20 옥시젯 구강세정기',
      u'브라운 전기면도기 7840S 시리즈7 정품 방수 충전식',
      u'브라운 보풀방지 펠트지/공예/교구/바느질/인형만들기/펠트diy',
      u'[일리커피머신]illy 일리 에스프레소 컵/에스프레소잔/일리잔[갤러리아]',
      u'피에르가르뎅 프리미엄 로얄 자동밸트 브라운 d7111a',
      u'[빨질레리] 브라운 트로피칼 조직 울 팬츠 (PA7121PF6D)',
      u'[Klein/클라인]- 브라운 핸드믹서',
      u'팸퍼스 베이비드라이 3~6단계 팬티 밴드기저귀',
      u'롯데 랩 골드 업소용 (30cm x500M) 포장랩 비닐랩 위',
    ]

  if len(titles) > 0:
    for title in titles:
      results = classify_title(title)
      category = ""
      for result in results:
        category += result + " "
      print title + " >> " + category

    print "4:5", str(compare_category(titles[4], titles[5]))
    print "4:6", str(compare_category(titles[4], titles[6]))
    print "4:7", str(compare_category(titles[4], titles[7]))
