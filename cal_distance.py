#-*- encoding: utf-8 -*-
import os
import pdb
import sys
from scipy.spatial import distance
reload(sys)
sys.setdefaultencoding('utf-8')

# if section is claim
def read_sentence_vectors(filename, firstline=False):
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
    if firstline: break
  for idx in range(len(av_vector)):
    av_vector[idx] /= num_vectors
  fin.close()

  return vectors, av_vector

# sum of min distances
def cal_cosine_wmd(vecs1, vecs2):
  sum_distance = 0
  for i1, vec1 in enumerate(vecs1):
    min_distance = 100
    min_idx = -1
    for i2, vec2 in enumerate(vecs2):
      cos_distance = distance.cosine(vec1, vec2)
      if min_distance > cos_distance:
        min_distance = cos_distance
        min_idx = i2
    sum_distance += min_distance
    #print str(i1) + ":" + str(min_idx) + " min distance is " + str(min_distance)
  return sum_distance

# min of min distances
def cal_cosine_mwmd(vecs1, vecs2):
  min_min_distance = 100
  min_idx1 = -1
  min_idx2 = -1
  for i1, vec1 in enumerate(vecs1):
    min_distance = 100
    min_idx = -1
    for i2, vec2 in enumerate(vecs2):
      cos_distance = distance.cosine(vec1, vec2)
      if min_distance > cos_distance:
        min_distance = cos_distance
        min_idx = i2 + 1
    if min_min_distance > min_distance:
      min_min_distance = min_distance
      min_idx1 = i1 + 1
      min_idx2 = min_idx
    #print str(i1) + ":" + str(min_idx) + " min distance is " + str(min_distance)
  return min_min_distance, min_idx1, min_idx2

# sum of min distances
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

# min of min distances
def cal_euclidean_mwmd(vecs1, vecs2):
  min_min_distance = 100
  for vec1 in vecs1:
    min_distance = 100
    for vec2 in vecs2:
      euc_distance = distance.euclidean(vec1, vec2)
      if min_distance > euc_distance:
        min_distance = euc_distance
    if min_min_distance > min_distance:
      min_min_distance = min_distance
  return min_min_distance

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "run with 2 arguments for a distance calculation (2 sentence vector files)"
    print "or run with 1 argument to find nearest neighbor (1 sentence vector file)"
    sys.exit()

  elif len(sys.argv) == 3:
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

  elif len(sys.argv) == 2:
    if not os.path.exists(sys.argv[1]):
      print "cannot find vector file"
      sys.exit()
    tokens = sys.argv[1].split("/")
    subdir = tokens[0]
    if subdir[-1] == "/":
      subdir = subdir[:-1]
    section = tokens[1]
    patent_id = tokens[-1].split("_")[0]
    vecs_dir = subdir + "/" + section + "/" 
    files = os.listdir(vecs_dir)
    if len(files) < 1:
      print "wrong patent vector directory: " + vecs_dir
      sys.exit()
    if section == "claims":
      vectors1, vector1 = read_sentence_vectors(sys.argv[1], True)  # only the firstline
    else:
      vectors1, vector1 = read_sentence_vectors(sys.argv[1])  # full lines
    rank1 = {}
    rank2 = {}
    rank3 = {}
    rank4 = {}
    count = 0
    for file in files:
      if file.endswith("vec"):
        print vecs_dir + file
        vectors2, vector2 = read_sentence_vectors(vecs_dir + file)

        #cos_distance_ave = distance.cosine(vector1, vector2)
        #rank1[file] = cos_distance_ave
        #euc_distance_ave = distance.euclidean(vector1, vector2)
        #rank2[file] = euc_distance_ave

        cos_distance_wmd, idx1, idx2 = cal_cosine_mwmd(vectors1, vectors2)
        rank3[file] = [cos_distance_wmd, idx1, idx2]
        #euc_distance_wmd = cal_euclidean_mwmd(vector1, vector2)
        #rank4[file] = cos_distance_wmd
        count += 1
        if count > 100000: break

    #fp = open(patent_id + "_" + tokens[1] + "_cos_ave_rank.txt", "w")
    #for f in sorted(rank1, key=rank1.get):
    #  fp.write(f + " " + str(rank1[f]) + "\n")
    #fp.close()

    #fp = open(patent_id + "_" + tokens[1] + "_euc_ave_rank.txt", "w")
    #for f in sorted(rank2, key=rank2.get):
    #  fp.write(f + " " + str(rank2[f]) + "\n")
    #fp.close()

    fp = open(patent_id + "_" + tokens[1] + "_cos_wmd_rank.txt", "w")
    for f in sorted(rank3, key=rank3.get):
      fp.write(f + " " + str(rank3[f]) + "\n")
    fp.close()

    #fp = open(patent_id + "_" + tokens[1] + "_euc_wmd_rank.txt", "w")
    #for f in sorted(rank4, key=rank4.get):
    #  fp.write(f + " " + str(rank4[f]) + "\n")
    #fp.close()
