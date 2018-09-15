#-*- encoding: utf-8 -*-
import requests
import math
import time
import random
from fake_useragent import UserAgent
import datetime
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

# Gets the patent numbers and stores them in a file
def get_patent_numbers(year1, month1, day1, year2, month2, day2):

    start_date = datetime.date(year1, month1, day1)
    stop_date = datetime.date(year2, month2, day2)
    date = start_date
    while date < stop_date:
        date_p1 = date + datetime.timedelta(days=1)
        after = date.strftime("%Y%m%d")
        before = date_p1.strftime("%Y%m%d")
         
        try:
            # Change "WO" to the name of the patent office.
            query = ("https://patents.google.com/xhr/query?url=country%3DKR%26language%3DKOREAN%26before%3Dfiling%3A" +
                before + "%26after%3D" + after + "%26num%3D100&exp=&download=true")
            print(query)

            # Sends the requests with random user agents and amounts of time between the requests
            sess = requests.Session()
            resp = sess.get(query, headers= headers)

            # Parses the pages, finds the patent numbers, and saves them to a file
            with open("timed_patents.csv", "a") as f:
                f.write(resp.content)

            # Rests a random amount of time before sending the next request
            time.sleep(random.randint(3,6))

        except KeyError:
            break

        date = date_p1


#Goes through the file, goes to the detailed patent page, downloads the relevant texts
def get_texts(file_name):
    with open(file_name, "r") as a:
        lines = a.readlines()

    s = requests.Session()
    s2 = requests.Session()

    for i in range(len(lines)):
        url = lines[i].strip()
        tokens = url.split("/")
        pnum = tokens[4]
        pfname = "timed_patents/html/" + pnum + ".html"
        if os.path.exists(pfname):
            print "file exists " + pfname
            continue

        try:
            r = s.get(url, headers=headers)
            print url 
        except Exception:
            print "cannot get the html " + url 
            continue

        kr = open(pfname, "w")
        kr.write(r.content)
        kr.close()
        time.sleep(random.randint(3,6))


# gets rid of duplicate patents and things that are not the name of a patent
def cleanse():
    fp = open("temp/timed_patents.csv", "r")
    lines = fp.readlines()
    fp.close()
    duplicate = []
    with open("temp/timed_patents.url","w") as f:
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

#get_patent_numbers(2016, 1, 1, 2017, 1, 1)
#cleanse()
get_texts("temp/2016_patents.url")
