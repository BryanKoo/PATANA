#-*- encoding: utf-8 -*-
import urllib
import requests
import math
import time
import random
from fake_useragent import UserAgent
import os.path
import sys, shutil
import pdb

# initialize values
page_number = 0
year = 0
month = 0
ua = UserAgent()
headers = {
            "user-agent" : ua.random,
          }

# search and download resulting csv file with patent numbers
def search_patents(year_begin, year_end, term):

  for year in range(year_begin, year_end):
    print(year)

    for month in range(1, 13):
      current_month = month
      one_more_month = month + 1
      if math.floor(month/10) == 0:
        current_month = "0" + str(month)
        one_more_month = "0" + str(one_more_month)
      one_more_year = year
      if one_more_month == 13:
        one_more_month = "01"
        one_more_year = year + 1

      try:
        # 1st ~ 15th day of the month
        query = u"https://patents.google.com/xhr/query?url=q=" + term + \
            "&country=KR&language=KOREAN&before=filing:" + str(year) + str(current_month) + \
            "16&after=" + str(year) + str(current_month) + "01" + "&num=100&exp=&download=true"
        query = urllib.quote(query.encode('utf8'), '/:?=&')
        print(query)
        pdb.set_trace()

        session = requests.Session()
        resp = session.get(query, headers= headers)
        with open("list/searched_patents.csv", "a") as f:
            f.write(resp.content)

        time.sleep(random.randint(3,6))

        # 16th ~ end of the month
        query = u"https://patents.google.com/xhr/query?url=q=" + term + \
            "&country=KR&language=KOREAN&before=filing:" + str(year) + str(current_month) + \
            "16&after="+ str(year) + str(current_month) + "01" + "&num=100&exp=&download=true"
        query = urllib.quote(query.encode('utf8'), '/:?=&')

        session = requests.Session()
        resp = session.get(query, headers= headers)
        with open("list/searched_patents.csv", "a") as f:
            f.write(resp.content)

        time.sleep(random.randint(3,6))

      except KeyError:
          break


# read the list, request and save each patent
def down_patent_htmls(subdir, filename):

  with open(filename, "r") as a:
    lines = a.readlines()

  session = requests.Session()

  for i in range(len(lines)):
    url = lines[i].strip()
    tokens = url.split("/")
    pnum = tokens[4]
    pfile = "searched_patents/html/" + subdir + "/" + pnum + ".html"
    tpfile = "timed_patents/html/" + pnum + ".html"

    if os.path.exists(tpfile):
      print "file exists " + tpfile
      shutil.copyfile(tpfile, pfile)
      continue

    try:
      r = session.get(url, headers=headers)
      print url
    except Exception:
      print "cannot get the html " + url
      continue

    kr = open(pfile, "w")
    kr.write(r.content)
    kr.close()
    time.sleep(random.randint(3,6))


# gets rid of duplicate patents and things that are not the name of a korean patent
def cleanse_list():
  fp = open("list/searched_patents.csv", "r")
  lines = fp.readlines()
  fp.close()
  duplicate = []
  with open("list/searched_patents.url","w") as f:
    for line in lines:
      columns = line.split(',')
      num = columns[0]
      if num == "search URL:" or num == "id":
        continue
      if num not in duplicate:
        duplicate.append(num)

        if "KR" in num:
          f.write("https://patents.google.com/patent/" + num.replace("-", "") + "/ko" + "\n")
        else:
          print("no KR: " + num)
      else:
        print("duplicated: " + num)

# default search years are from 2000 to 2016
# bitcoin 전자화폐 전자결제 블록체인 비트코인 가상화폐 암호화폐 전자지갑
# behicle 자율주행 비상제동 차선이탈 순항제어 주차보조 운전보조 크루즈콘트롤 무인자동차
# ai 인공지능 신경망 기계학습
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "run with command(search or download)"
    sys.exit()
  elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
      print "run with 1 or more search keywords seperated by space (use _ when space is needed within keyword)"
      sys.exit()
    keywords = ""
    for i in range(2, len(sys.argv)):
      keywords += sys.argv[i].decode('utf8') + ","
    keywords = keywords[:-1].replace("_", " ")
    search_patents(2000, 2017, keywords)
    cleanse_list()
    print "list/searched_patents.csv, list/searched_patents.url created"
    print "rename files for the separation from other searches"
  elif sys.argv[1] == "download":
    if len(sys.argv) < 4:
      print "run with url-list file and subdir"
      sys.exit()
    if os.path.exists(sys.argv[2]) and os.path.exists("searched_patents/html/" + sys.argv[3]):
      down_patent_htmls(sys.argv[3], sys.argv[2])
    else:
      print "cannot find url-list file and/or subdir"
  else:
    print "run with command(search or download)"
