from sklearn         import svm
from sklearn         import linear_model
from urllib2         import urlopen
from collections     import Counter
from sklearn.cluster import KMeans

import copy
import json
import math
import random
import numpy as np

DEFAULT_TSV_FILE            = 'instascrape.tsv'
DATUM_SPLIT_SIZE            = 18

IS_CREATED_COUNTRIES        = False
COUNTRIES_LIST              = []

IS_CREATED_CLUSTERS         = False
HAVERSINE_CLUSTERS          = {}

OVERESTIMATE_COUNTRY_NUMBER = 200

# INDIVIDUAL KEYS IN EACH DATA POINT DICT
#
# "image_id"                       -> str
# "image_creation_time"            -> int
# "image_comment_count"            -> int
# "tag_list"                       -> list of strs
# "filter_type"                    -> str
# "location_longitude"             -> float
# "location_latitude"              -> float
# "location_name"                  -> str
# "caption_text"                   -> str
# "likes_count"                    -> int
# "user_username"                  -> str
# "user_id"                        -> int
# "comment_time_text_encoding"     -> list of (time,text) tuples
# "user_media_count"               -> int
# "user_followed_by_count"         -> int
# "user_follows_count"             -> int
# "user_followed_by_ids_encoding"  -> list of ints
# "user_follows_ids_encoding"      -> list of ints
#
# (returned data list is a list of dicts, each 
# corresponding to one image's worth of metadata)




# QUICK RUN THROUGH GUIDE
# Basically, assuming the instascrape.tsv is in the same directory as this file, here's what you'd enter in a terminal:
#
# python
# import feature_extraction as fe
# data = fe.extract_from_tsv()
# location_data  = fe.location_tagged_dataset(data)
# feature_vector = fe.create_feature_vector(data) # it's here where we input a list of feature extractors, right now it's a default if you see the definition below
# x_data, y_data = feature_vector
# score = fe.apply_machine_learning_algorithm(x_data, y_data) 
# print score

# loc = fe.location_tagged_dataset(fe.extract_from_tsv())
# vec = fe.location_clustering_distance(loc,loc[0])

def extract_from_tsv(filename=DEFAULT_TSV_FILE, max_limit = None):
  f         = open(filename, 'r')
  key_line  = f.readline()
  key_names = key_line.strip().split('\t')

  data      = []
  count     = 0

  for line in f:
    valid_datum = True
    try:
      d = line.strip().split('\t')

      if len(d) != DATUM_SPLIT_SIZE:
        valid_datum = False

      if d[0] == "image_id":
        valid_datum = False

      datum = {}

      for n in xrange(DATUM_SPLIT_SIZE):
        data_chunk = None
        key_name   = key_names[n]

        if   n == 0:
          data_chunk = str(d[n])
        elif n == 1:
          data_chunk = int(d[n])
        elif n == 2:
          data_chunk = int(d[n])
        elif n == 3:
          if d[n] != '[]':
            data_chunk = eval(d[n])
        elif n == 4:
            data_chunk = str(d[n])
        elif n == 5:
          if d[n] != "-BLANK-":
            data_chunk = float(d[n])
        elif n == 6:
          if d[n] != "-BLANK-":
            data_chunk = float(d[n])
        elif n == 7:
          if d[n] != "-BLANK-":
            data_chunk = str(d[n])
        elif n == 8:
          if d[n] != "CAPTION_TEXT":
            data_chunk = str(d[n])
        elif n == 9:
          data_chunk = int(d[n])
        elif n == 10:
          data_chunk = str(d[n])
        elif n == 11:
          data_chunk = int(d[n])
        elif n == 12:
          try:
            time_text_pairs = d[n].split('{}')
            data_chunk = []
            for pair in time_text_pairs:
              colon_index = pair.find(':')
              time = pair[0:colon_index]
              text = pair[colon_index+1:-1]
              data_chunk.append((time,text))
          except:
            pass
        elif n == 13:
          data_chunk = int(d[n])
        elif n == 14:
          data_chunk = int(d[n])
        elif n == 15:
          data_chunk = int(d[n])
        elif n == 16:
          data_chunk = [ int(x) for x in d[n].split('{}') ]
        else:
          data_chunk = [ int(x) for x in d[n].split('{}') ]

        datum[key_name] = data_chunk

      if valid_datum:
        data.append(datum)
        count += 1
      if max_limit != None and count >= max_limit:
        break

    except:
      pass

  print "Total data points: " + str(count)
  return data



def location_tagged_dataset(dataset):
  location_tagged_data = []

  for ind in xrange(len(dataset)):
    if dataset[ind]["location_longitude"] is not None and dataset[ind]["location_latitude"] is not None:
      location_tagged_data.append(copy.deepcopy(dataset[ind]))

  print "Total data points: " + str(len(location_tagged_data))
  return location_tagged_data



# Just simple numbered data that can easily be extracted

def basic_numerical_feature_extractor(data_point):
  feature_vector     = []
  numerics_data_keys = ["image_comment_count","user_media_count","user_followed_by_count","user_follows_count"]

  for data_key in numerics_data_keys:
    feature_vector.append(data_point[data_key])

  return feature_vector



# 'sentiment analysis' w/ tags, captions, comment (time,text) tuples

def sentiment_analysis():

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  raise Exception("Not implemented yet")
  # END_YOUR_CODE

  return None



# 'location clustering' by country in which it is located

def location_clustering_country(location_dataset, data_point):

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  def get_place(lat, lon):
    """
    Determine the country to which the latitude and
    longitude belong to, or return None
    """
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    #return town, country
    return country

  def create_total_countries_list(dataset):
    countries_dict = Counter()
    for datum in dataset:
      latitude  = datum['location_latitude']
      longitude = datum['location_longitude']
      country   = get_place(latitude, longitude)
      countries_dict[country] += 1
    countries_list = countries_dict.keys()
    return sorted(countries_list)

  global IS_CREATED_COUNTRIES
  global COUNTRIES_LIST

  if not IS_CREATED_COUNTRIES:
    COUNTRIES_LIST = create_total_countries_list(location_dataset)
    IS_CREATED_COUNTRIES = True

  country_vector = [0] * OVERESTIMATE_COUNTRY_NUMBER
  latitude  = data_point['location_latitude']
  longitude = data_point['location_longitude']
  country   = get_place(latitude, longitude)
  country_vector[COUNTRIES_LIST.index(country)] = 1

  # END_YOUR_CODE
  
  return country_vector



# 'location cluster' by haversine distance between lon/lat

def location_clustering_distance(dataset, data_point, k_clusters=10):

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  def haversine(pt1,pt2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1 = float(pt1['location_longitude'])
    lat1 = float(pt1['location_latitude'])
    lon2 = float(pt2['location_longitude'])
    lat2 = float(pt2['location_latitude'])
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km 

  def kmeans_cluster_by_distance(data, k_val): 
    cluster_mapping = {}

    centroids = random.sample(range(len(data)), k_val)
    
    iters = 100
    while iters > 0:
      print iters
      iters -= 1
      clusters = dict()
      for centroid in centroids:
        #key = frozenset((float(centroid['location_longitude']),float(centroid['location_latitude'])))
        #clusters[key] = set()
        clusters[centroid] = []

      print clusters.keys() ##################################################

      for ind in range(len(data)):
        if ind in centroids:
          best_ind, best_dist = ind, 0
        else:
          best_ind, best_dist = 0, float("inf")
          for centroid in centroids[1:]:
            if haversine(data[ind], data[centroid]) < best_dist:
              best_ind, best_dist = centroid, haversine(data[ind], data[centroid])
        #key = frozenset((float(best_datum['location_longitude']),float(best_datum['location_latitude'])))
        #print key
        clusters[best_ind].append(ind)

      new_centroids = []
      for key, cluster in clusters.iteritems():
        best_ind, best_dist = 0, float("inf")
        for ind in cluster:
          # lowest sum of distance
          dist = sum([ haversine(data[ind], data[pt]) for pt in cluster ])
          if dist < best_dist:
            best_ind, best_dist = ind, dist
        new_centroids.append(best_ind)

      if sorted(new_centroids) == sorted(centroids):
        break
      else:
        centroids = new_centroids

    clusters_listified = [ list(clusters[key]) for key in clusters.keys() ]
    clusters_listified = sorted(clusters_listified, key=len(points))
    for i in xrange(k_val):
      cluster_mapping[i] = clusters_listified[i]
      print "Cluster "+str(i)+" has "+str(len(clusters_listified[i]))+" points."

    return cluster_mapping
  
  global IS_CREATED_CLUSTERS
  global HAVERSINE_CLUSTERS

  if not IS_CREATED_CLUSTERS:
    HAVERSINE_CLUSTERS  = kmeans_cluster_by_distance(dataset, k_clusters)
    IS_CREATED_CLUSTERS = True

  cluster_vector = [0] * k_clusters
  for key, points in HAVERSINE_CLUSTERS.items():
    ind = dataset.index(data_point)
    if ind in points:
      cluster_vector[key] = 1
      break

  # END_YOUR_CODE
  
  return cluster_vector



# 'image relevancy' w/ (last comment time - image creation time), comment count, comment (time,text) tuples, followed by count, likes count

def image_relevancy():

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  raise Exception("Not implemented yet")
  # END_YOUR_CODE
  
  return None



# 'association rules' w/ image, filter, location

def association_rules():

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  raise Exception("Not implemented yet")
  # END_YOUR_CODE
  
  return None



def create_feature_vector(dataset, target_variable="likes_count", extractor_funcs=[basic_numerical_feature_extractor]):
  # If we have feature extraction functions, apply them here,
  # and create mega vector to be fed into final algorithm.
  # 
  # target_variable is what we are trying to predict
  #
  # NOTE: only take in location based extractors if the dataset
  # passed in is a location dataset

  x_data = []
  y_data = []

  for datum in dataset:

    x_datum = []

    # apply extraction to a datapoint, append to x_datum
    for extractor_func in extractor_funcs:
      x_datum.append(extractor_func(datum))

    x_datum = [ sub_datum for sub_x_datum in x_datum for sub_datum in sub_x_datum ]

    x_data.append(x_datum)
    y_data.append(datum[target_variable])

  return (x_data,y_data)



def apply_machine_learning_algorithm(x_dataset, y_dataset, ml_func=linear_model.LinearRegression(), split_proportion=0.20, permute=False, cross_validate=False):
  # Assumes the use of a ML supervised algorithm
  # Split proportion governs how much to reserve for test set
  # We will also introduce k-folds cross-validation when we have time to let this run for a while
  #
  # IMPORTANT NOTE: the data is naively split right now, but first
  # we will need to permute the datasets before splitting, since
  # the data was collected (an assumption with the scraper) in
  # chronological order - need to avoid "hidden recency" correlations with a naive split
  #
  # Try:
  # Linear Regression
  # Decision Tree
  # SVM

  split_point = int(len(x_dataset)*split_proportion)

  #TODO: automatic k-fold cross-validation and stats output
  #TODO: training vs. testing graph by iteration
  # perhaps a good time for 2D PCA #TODO: add pca graphing

  X_train = np.array(x_dataset[split_point:-1])
  Y_train = np.array(y_dataset[split_point:-1])

  if permute:
    random.seed(37)
    random.shuffle(X_train)
    random.seed(37)
    random.shuffle(Y_train)

  X_test  = np.array(x_dataset[0:split_point])
  Y_test  = np.array(y_dataset[0:split_point])



  ml_func.fit(X_train, Y_train)

  score = ml_func.score(X_test,Y_test)

  #return (X_train,Y_train,X_test,Y_test)
  return score



# 1) geolocation clustering
# 2) longitude/latitude k-means clustering
# 3) decision tree


# NOTES: 
#
# OBVIOUS FEATURES:
#
# filter_type
# likes_count
# image_comment_count
# user_followed_by_count
# user_follows_count
# user_media_count
#
# EXPERIMENTAL FEATURES:
#
# 'network measurements' w/ followed/follows ids
# 'burstiness' w/ comment (time,text) tuples

#TODO: autorun style function for quick execution of location vs. no location, etc., does LinReg, DecTre, SVM with location vs. no location, graphs everything for easy comparison, and auto-ablation with selective feature creation

