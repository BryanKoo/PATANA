#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
sys.path.append("/home/khkoo")
from textutil.alphabet import has_hanja, has_hangul, has_alpha
from utils.sentence_segmenter_en import sentence_segmenter
from konlpy.tag import Mecab
mecab = Mecab()
reload(sys)
sys.setdefaultencoding('utf-8')

def sbd_text(filename, fulltext=True):
  fin = open(filename, "r")
  if fulltext: fout = open(filename[:-4] + "_sbd.txt", "w")
  fout2 = open(filename[:-4] + "_sbd_words.txt", "w")
  while True:
    line = fin.readline().decode("utf-8")
    if not line: break
    line = line.strip()
    if line == "": continue
    if not has_hangul(line): continue

    # 쉼표로 끝나면 다음줄 붙이기
    while line.endswith(r","):
      line += " " + fin.readline().decode("utf-8").strip()

    # 괄호열기 후에 괄호닫기가 없고 문장부호 없다면 다음줄 붙이기
    while line.count("(") > line.count(")"):
      if line.endswith(".") or line.endswith("?") or line.endswith("!"): break
      next_line = fin.readline().decode("utf-8").strip()
      if not next_line: break
      next_line = next_line.strip()
      if next_line == "": break
      if not has_hangul(next_line): break
      line += " " + next_line

    lines = sentence_segmenter(line, "ko")
    for line in lines:
      if fulltext: fout.write(line + "\n")
      fout2.write(remove_stopword(line) + "\n")
  if fulltext: fout.close()
  fout2.close()
  if not fulltext:
    os.remove(filename)

def remove_stopword(line):
  line = line.replace(";", ",")
  phrases = line.split(",")
  out_line = ""
  for phrase in phrases:
    words = phrase.split(" ")
    for word in words:
      copy_word = ""
      tokens_pos = mecab.pos(word)
      prev_nn = False
      for i, token_pos in enumerate(tokens_pos):
        token = token_pos[0]
        pos = token_pos[1]
        if pos.startswith("SF") or pos.startswith("SE") or pos.startswith("SY") or pos.startswith("SC"):  # 기호 제거
          continue
        elif pos.startswith("SS"):  # 괄호 제거
          break
        elif pos.startswith("J"): # 조사 제거
          break
        else:
          copy_word += token
      if copy_word != "":
        out_line += copy_word + " "
  return out_line.strip()


if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for subdir (searched_patents, timed_patents) and section (abstract, description, claims, sentences)"
    sys.exit()
  filename = sys.argv[1] + "/" + sys.argv[2] + ".txt"
  #sbd_text(filename)
  text_dir = sys.argv[1] + "/" + sys.argv[2] + "/"
  files = os.listdir(text_dir)
  if len(files) < 1:
    print "wrong patent directory: " + text_dir
    sys.exit()
  for file in files:
    if file.endswith("txt") and not file.endswith("words.txt"):
      print file
      sbd_text(text_dir + file, False)
