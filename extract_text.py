#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_texts(file_name):
  first_slash = file_name.find("/")
  num_start = file_name.rfind("/")
  num_stop = file_name.find(".")
  patent_type = file_name[:first_slash]
  patent_num = file_name[num_start+1:num_stop]
  
  print file_name

  with open(file_name, "r") as a:
    html = a.read()

  text = open(patent_type + "/text/" + patent_num + ".txt", "w")

  soup = BeautifulSoup(html, "lxml")
  article = soup.find("article")

  # title
  title = article.span.text.strip()
  text.write("!!!title\n" + title + "\n")

  abstract_section = article.find("section", itemprop="abstract")
  description_section = article.find("section", itemprop="description")
  claims_section = article.find("section", itemprop="claims")

  # classification
  classifications = ""
  classification_h2 = article.find("h2", text="Classifications")
  if classification_h2 != None:
    classification_spans = classification_h2.find_next().findAll("span", itemprop="Code")
    for span in classification_spans:
      classifications += span.text + " "
    classifications = classifications.strip()
    text.write("!!!classifications\n" + classifications + "\n")
    if classifications == "":
      print "!!cannot find classifications with h2"
      pdb.set_trace()
  
  # abstract
  abstract = abstract_section.div.abstract.div.text.strip()
  text.write("!!!abstract\n" + abstract + "\n")

  # prepare text of description_section because there are many formats (worst case: invention-title and p tags)
  description = ""
  description_div = description_section.find("div", {"class":"description"})
  if description_div == None:
    print "no description"
    pdb.set_trace()
  description_ps = description_div.findAll("p")
  for p in description_ps:
    if "num" in p.attrs:
      if p.text.strip() != "":
        description += p.text.strip() + "\n"

  # technical field
  field = ""
  if description_section.find("technical-field") != None:
    field = description_section.find("technical-field").text.strip()
    text.write("!!!field\n" + field + "\n")

  # background art
  background = ""
  if description_section.find("background-art") != None:
    background = description_section.find("background-art").text.strip() 
    text.write("!!!background\n" + background + "\n")

  # tech problem
  problem = ""
  if description_section.find("tech-problem") != None:
    problem = description_section.find("tech-problem").text.strip() 
    text.write("!!!problem\n" + problem + "\n")

  # tech solution
  solution = ""
  if description_section.find("tech-solution") != None:
    solution = description_section.find("tech-solution").text.strip() 
    text.write("!!!solution\n" + solution + "\n")

  # advantages
  advantages = ""
  if description_section.find("advantageous-effects") != None:
    advantages = description_section.find("advantageous-effects").text.strip()
    text.write("!!!adbantages\n" + advantages + "\n")

  # applicability
  applicability = ""
  if description_section.find("industrial-applicability") != None:
    applicability = description_section.find("industrial-applicability").text.strip()
    text.write("!!!applicability\n" + applicability + "\n")

  # description of drawings
  drawings = ""
  if description_section.find("description-of-drawings") != None:
    drawings = description_section.find("description-of-drawings").text.strip()
    text.write("!!!drawings\n" + drawings + "\n")

  # embodiments
  embodiments = ""
  if description_section.find("description-of-embodiments") != None:
    embodiments = description_section.find("description-of-embodiments").text.strip()
    text.write("!!!embodiments\n" + embodiments + "\n")

  # disclosure
  disclosure = ""
  if description_section.find("disclosure") != None:
    disclosure = description_section.find("disclosure").text.strip()
    text.write("!!!disclosure\n" + disclosure + "\n")

  # summary
  summary = ""
  if description_section.find("summary-of-invention") != None:
    summary = description_section.find("summary-of-invention").text.strip()
    text.write("!!!summary\n" + summary + "\n")

  # sequence
  sequence = ""
  if description_section.find("sequence-list-text") != None:
    sequence = description_section.find("sequence-list-text").text.strip()
    text.write("!!!sequence\n" + sequence + "\n")

  # modes
  modes = ""
  if description_section.find("mode-for-invention") != None:
    modes = description_section.find("mode-for-invention").text.strip()
    text.write("!!!modes\n" + modes + "\n")

  # terms
  terms = ""
  if description_section.find("reference-signs-list") != None:
    terms = description_section.find("reference-signs-list").text.strip()
    text.write("!!!terms\n" + terms + "\n")

  # no separated description
  if embodiments == "" and solution == "" and disclosure == "" and summary == "" and sequence == "" and modes == "" and field == "":
    text.write("!!!description\n" + description)

  # claims
  claims = ""
  lis = claims_section.findAll("li")
  if len(lis) > 0:
    for li in lis:
      claim = li.text.strip()
      if claim != u"삭제":
        claims += claim + "\n"
  else:
    divs = claims_section.findAll("div", {"class":"claim-text"})
    for div in divs:
      claim = div.text.strip()
      if claim != u"삭제":
        claims += claim + "\n"
  text.write("!!!claims\n" + claims)

  text.close()

  if title == "":
    print "cannot find title"
    pdb.set_trace()
  if claims == "":
    print "cannot find claims"
    pdb.set_trace()


html_dir = "searched_patents/html/"
files = os.listdir(html_dir)
for file in files:
  if file.endswith("html"):
    get_texts(html_dir + file)
