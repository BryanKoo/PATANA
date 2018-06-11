#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import pdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# all, abstract, description(including abstract), claims
def get_texts(file_name, parts="all"):
  first_slash = file_name.find("/")
  num_start = file_name.rfind("/")
  num_stop = file_name.find(".")
  patent_type = file_name[:first_slash]
  patent_num = file_name[num_start+1:num_stop]
  has_text = False
  
  print file_name

  with open(file_name, "r") as a:
    html = a.read()

  soup = BeautifulSoup(html, "lxml")
  article = soup.find("article")

  # classification
  classifications = ""
  classification_h2 = article.find("h2", text="Classifications")
  if classification_h2 != None:
    classification_spans = classification_h2.find_next().findAll("span", itemprop="Code")
    for span in classification_spans:
      classifications += span.text + " "
    classifications = classifications.strip()
    if classifications.startswith("A") or classifications.startswith("C") or classifications.startswith("D") or classifications.startswith("F"):
      print "irrelevant patent"
      return

  text = open(patent_type + "/text/" + patent_num + ".txt", "w")

  if classifications != "":
    if parts == "all":
      has_text = True
      text.write("!!!classifications\n" + classifications + "\n")
  
  # title
  title = article.span.text.strip()
  if parts == "all":
    has_text = True
    text.write("!!!title\n" + title + "\n")

  abstract_section = article.find("section", itemprop="abstract")
  description_section = article.find("section", itemprop="description")
  claims_section = article.find("section", itemprop="claims")

  # abstract
  abstract = abstract_section.div.abstract.div.text.strip()
  if parts == "abstract" or parts == "sentences":
    has_text = True
    text.write(abstract + "\n")
  elif parts == "all":
    has_text = True
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

  # technical field (발명이 이루고자 하는 기술적 과제)(기술분야)
  field = ""
  if description_section.find("technical-field") != None:
    field = description_section.find("technical-field").text.strip()
    if parts == "description" or parts == "sentences":
      has_text = True
      text.write(field + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!field\n" + field + "\n")

  # background art (발명이 속하는 기술 및 그 분야의 종래기술)(배경기술)
  background = ""
  if description_section.find("background-art") != None:
    background = description_section.find("background-art").text.strip() 
    if parts == "description" or parts == "sentences":
      has_text = True
      text.write(background + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!background\n" + background + "\n")

  # tech problem
  problem = ""
  if description_section.find("tech-problem") != None:
    problem = description_section.find("tech-problem").text.strip() 
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(problem + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!problem\n" + problem + "\n")

  # tech solution (발명의 구성 및 작용)
  solution = ""
  if description_section.find("tech-solution") != None:
    solution = description_section.find("tech-solution").text.strip() 
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(solution + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!solution\n" + solution + "\n")

  # advantages (발명의 효과)
  advantages = ""
  if description_section.find("advantageous-effects") != None:
    advantages = description_section.find("advantageous-effects").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(advantages + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!advantages\n" + advantages + "\n")

  # applicability (산업상 이용 가능성)
  applicability = ""
  if description_section.find("industrial-applicability") != None:
    applicability = description_section.find("industrial-applicability").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(applicability + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!applicability\n" + applicability + "\n")

  # description of drawings
  drawings = ""
  if description_section.find("description-of-drawings") != None:
    drawings = description_section.find("description-of-drawings").text.strip()
    if parts == "all":
      has_text = True
      text.write("!!!drawings\n" + drawings + "\n")

  # embodiments (발명의 상세한 설명)
  embodiments = ""
  if description_section.find("description-of-embodiments") != None:
    embodiments = description_section.find("description-of-embodiments").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(embodiments + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!embodiments\n" + embodiments + "\n")

  # disclosure (may overlap with tech-solution, advantageous-effects)
  disclosure = ""
  if solution == "" and description_section.find("disclosure") != None:
    disclosure = description_section.find("disclosure").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(disclosure + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!disclosure\n" + disclosure + "\n")

  # summary
  summary = ""
  if description_section.find("summary-of-invention") != None:
    summary = description_section.find("summary-of-invention").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(summary + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!summary\n" + summary + "\n")

  # sequence
  sequence = ""
  if description_section.find("sequence-list-text") != None:
    sequence = description_section.find("sequence-list-text").text.strip()
    if parts == "all":
      has_text = True
      text.write("!!!sequence\n" + sequence + "\n")

  # modes
  modes = ""
  if description_section.find("mode-for-invention") != None:
    modes = description_section.find("mode-for-invention").text.strip()
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(modes + "\n")
    elif parts == "all":
      has_text = True
      text.write("!!!modes\n" + modes + "\n")

  # terms
  terms = ""
  if description_section.find("reference-signs-list") != None:
    terms = description_section.find("reference-signs-list").text.strip()
    if parts == "all":
      has_text = True
      text.write("!!!terms\n" + terms + "\n")

  # no separated description
  if embodiments == "" and solution == "" and disclosure == "" and summary == "" and modes == "" and field == "":
    if parts == "sentences" or parts == "description":
      has_text = True
      text.write(description)
    elif parts == "all":
      has_text = True
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
  if parts == "sentences" or parts == "claims":
    has_text = True
    text.write(claims)
  elif parts == "all":
    has_text = True
    text.write("!!!claims\n" + claims)

  text.close()

  if title == "":
    print "cannot find title"
    pdb.set_trace()
  if claims == "":
    print "cannot find claims"
    pdb.set_trace()
  if not has_text:
    print "cannot find text"
    pdb.set_trace()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for patent directory(searched_patents, timed_patents) and type of extraction(abstract, description, claims, sentences, all)"
    sys.exit()
  html_dir = sys.argv[1] + "/html/"
  files = os.listdir(html_dir)
  if len(files) < 1:
    print "wrong patent directory: " + sys.argv[1]
    sys.exit()
  for file in files:
    if file.endswith("html"):
      size = os.path.getsize(html_dir + file)
      if size > 2784238:
        os.remove(html_dir + file)
      else:
        get_texts(html_dir + file, sys.argv[2])
