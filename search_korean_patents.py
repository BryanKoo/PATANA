#-*- encoding: utf-8 -*-
import urllib
import requests
import math
import time
import random
from fake_useragent import UserAgent
import os.path
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
            "16&after="+ str(year) + str(current_month) + "01" + "&num=100&exp=&download=true"
        query = urllib.quote(query.encode('utf8'), '/:?=&')
        print(query)

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
def get_patent_htmls(file_name):

  with open(file_name, "r") as a:
    lines = a.readlines()

  session = requests.Session()

  for i in range(len(lines)):
    url = lines[i].strip()
    tokens = url.split("/")
    pnum = tokens[4]
    pfname = "searched_patents/html/" + pnum + ".html"
    if os.path.exists(pfname):
      print "file exists " + pfname
      continue

    try:
      r = session.get(url, headers=headers)
      print url
    except Exception:
      print "cannot get the html " + url
      continue

    kr = open(pfname, "w")
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

if __name__ == "__main__":
  search_patents(2000, 2017, u"전자화폐,전자결제,블록체인,비트코인,가상화폐,암호화폐,전자지갑")
  search_patents(2000, 2017, u"자율주행,비상제동,차선이탈,순항제어,주차보조,운전보조,크루즈콘트롤,무인자동차")
  search_patents(2000, 2017, u"인공지능,신경망,기계학습")
  cleanse_list()
  get_patent_htmls("list/searched_patents.url")
