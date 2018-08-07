#-*- encoding: utf-8 -*-
import os
import pdb
import sys
from scipy.spatial import distance
reload(sys)
sys.setdefaultencoding('utf-8')

def read_sentence_vectors(filename):
  vectors = []
  av_vector = []
  num_vectors = 0
  fin = open(filename, "r")
  while True:
    line = fin.readline().decode("utf-8")
    if not line: break
    line = line.strip()
    if line == "": continue
    if line.find("-nan") >= 0: continue
    vec_tokens = line.split(" ")
    tokens = vec_tokens[-100:]
    vector = []
    for token in tokens:
      vector.append(float(token))
    vectors.append(vector)
    num_vectors += 1
    if num_vectors == 1: av_vector = vector
    else:
      for idx in range(len(av_vector)):
        av_vector[idx] += vector[idx]
  for idx in range(len(av_vector)):
    av_vector[idx] /= num_vectors
  fin.close()

  return vectors, av_vector

def cal_cosine_wmd(vecs1, vecs2):
  total_distance = 0
  for vec1 in vecs1:
    min_distance = 100
    for vec2 in vecs2:
      cos_distance = distance.cosine(vec1, vec2)
      if min_distance > cos_distance:
        min_distance = cos_distance
    total_distance += min_distance
  return total_distance

def cal_euclidean_wmd(vecs1, vecs2):
  total_distance = 0
  for vec1 in vecs1:
    min_distance = 100
    for vec2 in vecs2:
      euc_distance = distance.euclidean(vec1, vec2)
      if min_distance > euc_distance:
        min_distance = euc_distance
    total_distance += min_distance
  return total_distance

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "run with 2 arguments for two sentence vector files or 3 arguments (file, subdirectory, part)"
    sys.exit()

  if len(sys.argv) == 3:
    if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
      print "cannot find vector files"
      sys.exit()
    vectors1, vector1 = read_sentence_vectors(sys.argv[1])
    vectors2, vector2 = read_sentence_vectors(sys.argv[2])
    
    cos_distance_ave = distance.cosine(vector1, vector2)
    print "cosine distance of average " + str(cos_distance_ave)
    euc_distance_ave = distance.euclidean(vector1, vector2)
    print "euclidean distance of average " + str(euc_distance_ave)

    cos_distance_wmd = cal_cosine_wmd(vectors1, vectors2)
    print "cosine distance of wmd for " + str(len(vectors1)) + " vectors is " + str(cos_distance_wmd)
    euc_distance_wmd = cal_euclidean_wmd(vector1, vector2)
    print "euclidean distance of wmd for " + str(len(vectors1)) + " vectors is " + str(euc_distance_wmd)
  elif len(sys.argv) == 4:
    if not os.path.exists(sys.argv[1]):
      print "cannot find vector file"
      sys.exit()
    patent_str = sys.argv[1].split("/")[-1]
    patent_id = patent_str.split("_")[0]
    text_dir = sys.argv[2] + "/" + sys.argv[3] + "/" 
    files = os.listdir(text_dir)
    if len(files) < 1:
      print "wrong patent directory: " + text_dir
      sys.exit()
    vectors1, vector1 = read_sentence_vectors(sys.argv[1])
    rank1 = {}
    rank2 = {}
    rank3 = {}
    rank4 = {}
    count = 0
    for file in files:
      if file.endswith("vec"):
        print text_dir + file
        vectors2, vector2 = read_sentence_vectors(text_dir + file)
        cos_distance_ave = distance.cosine(vector1, vector2)
        print "cosine distance of average " + str(cos_distance_ave)
        euc_distance_ave = distance.euclidean(vector1, vector2)
        print "euclidean distance of average " + str(euc_distance_ave)

        cos_distance_wmd = cal_cosine_wmd(vectors1, vectors2)
        print "cosine distance of wmd for " + str(len(vectors1)) + " vectors is " + str(cos_distance_wmd)
        euc_distance_wmd = cal_euclidean_wmd(vector1, vector2)
        print "euclidean distance of wmd for " + str(len(vectors1)) + " vectors is " + str(euc_distance_wmd)
        print ""
        rank1[file] = cos_distance_ave
        rank2[file] = euc_distance_ave
        rank3[file] = cos_distance_wmd
        rank4[file] = cos_distance_wmd
        count += 1
        if count > 100000: break
    fp = open(patent_id + "_" + sys.argv[3] + "_cos_ave_rank.txt", "w")
    for f in sorted(rank1, key=rank1.get):
      fp.write(f + " " + str(rank1[f]) + "\n")
    fp.close()
    fp = open(patent_id + "_" + sys.argv[3] + "_euc_ave_rank.txt", "w")
    for f in sorted(rank2, key=rank2.get):
      fp.write(f + " " + str(rank2[f]) + "\n")
    fp.close()
    fp = open(patent_id + "_" + sys.argv[3] + "_cos_wmd_rank.txt", "w")
    for f in sorted(rank3, key=rank3.get):
      fp.write(f + " " + str(rank3[f]) + "\n")
    fp.close()
    fp = open(patent_id + "_" + sys.argv[3] + "_euc_wmd_rank.txt", "w")
    for f in sorted(rank4, key=rank4.get):
      fp.write(f + " " + str(rank4[f]) + "\n")
    fp.close()
