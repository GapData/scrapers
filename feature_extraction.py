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


# Afghanistan Kabul 34°28'N 69°11'E
# Albania Tirane  41°18'N 19°49'E
# Algeria Algiers 36°42'N 03°08'E
# American Samoa  Pago Pago 14°16'S 170°43'W
# Andorra Andorra la Vella  42°31'N 01°32'E
# Angola  Luanda  08°50'S 13°15'E
# Antigua and Barbuda W. Indies 17°20'N 61°48'W
# Argentina Buenos Aires  36°30'S 60°00'W
# Armenia Yerevan 40°10'N 44°31'E
# Aruba Oranjestad  12°32'N 70°02'W
# Australia Canberra  35°15'S 149°08'E
# Austria Vienna  48°12'N 16°22'E
# Azerbaijan  Baku  40°29'N 49°56'E
# Bahamas Nassau  25°05'N 77°20'W
# Bahrain Manama  26°10'N 50°30'E
# Bangladesh  Dhaka 23°43'N 90°26'E
# Barbados  Bridgetown  13°05'N 59°30'W
# Belarus Minsk 53°52'N 27°30'E
# Belgium Brussels  50°51'N 04°21'E
# Belize  Belmopan  17°18'N 88°30'W
# Benin Porto-Novo (constitutional cotonou) (seat of gvnt)  06°23'N 02°42'E
# Bhutan  Thimphu 27°31'N 89°45'E
# Bolivia La Paz (adm.)/sucre (legislative) 16°20'S 68°10'W
# Bosnia and Herzegovina  Sarajevo  43°52'N 18°26'E
# Botswana  Gaborone  24°45'S 25°57'E
# Brazil  Brasilia  15°47'S 47°55'W
# British Virgin Islands  Road Town 18°27'N 64°37'W
# Brunei Darussalam Bandar Seri Begawan 04°52'N 115°00'E
# Bulgaria  Sofia 42°45'N 23°20'E
# Burkina Faso  Ouagadougou 12°15'N 01°30'W
# Burundi Bujumbura 03°16'S 29°18'E
# Cambodia  Phnom Penh  11°33'N 104°55'E
# Cameroon  Yaounde 03°50'N 11°35'E
# Canada  Ottawa  45°27'N 75°42'W
# Cape Verde  Praia 15°02'N 23°34'W
# Cayman Islands  George Town 19°20'N 81°24'W
# Central African Republic  Bangui  04°23'N 18°35'E
# Chad  N'Djamena 12°10'N 14°59'E
# Chile Santiago  33°24'S 70°40'W
# China Beijing 39°55'N 116°20'E
# Colombia  Bogota  04°34'N 74°00'W
# Comros  Moroni  11°40'S 43°16'E
# Congo Brazzaville 04°09'S 15°12'E
# Costa Rica  San Jose  09°55'N 84°02'W
# Cote d'Ivoire Yamoussoukro  06°49'N 05°17'W
# Croatia Zagreb  45°50'N 15°58'E
# Cuba  Havana  23°08'N 82°22'W
# Cyprus  Nicosia 35°10'N 33°25'E
# Czech Republic  Prague  50°05'N 14°22'E
# Democratic People's Republic of P'yongyang  39°09'N 125°30'E
# Democratic Republic of the Congo  Kinshasa  04°20'S 15°15'E
# Denmark Copenhagen  55°41'N 12°34'E
# Djibouti  Djibouti  11°08'N 42°20'E
# Dominica  Roseau  15°20'N 61°24'W
# Dominica Republic Santo Domingo 18°30'N 69°59'W
# East Timor  Dili  08°29'S 125°34'E
# Ecuador Quito 00°15'S 78°35'W
# Egypt Cairo 30°01'N 31°14'E
# El Salvador San Salvador  13°40'N 89°10'W
# Equatorial Guinea Malabo  03°45'N 08°50'E
# Eritrea Asmara  15°19'N 38°55'E
# Estonia Tallinn 59°22'N 24°48'E
# Ethiopia  Addis Ababa 09°02'N 38°42'E
# Falkland Islands (Malvinas) Stanley 51°40'S 59°51'W
# Faroe Islands Torshavn  62°05'N 06°56'W
# Fiji  Suva  18°06'S 178°30'E
# Finland Helsinki  60°15'N 25°03'E
# France  Paris 48°50'N 02°20'E
# French Guiana Cayenne 05°05'N 52°18'W
# French Polynesia  Papeete 17°32'S 149°34'W
# Gabon Libreville  00°25'N 09°26'E
# Gambia  Banjul  13°28'N 16°40'W
# Georgia T'bilisi  41°43'N 44°50'E
# Germany Berlin  52°30'N 13°25'E
# Ghana Accra 05°35'N 00°06'W
# Greece  Athens  37°58'N 23°46'E
# Greenland Nuuk  64°10'N 51°35'W
# Guadeloupe  Basse-Terre 16°00'N 61°44'W
# Guatemala Guatemala 14°40'N 90°22'W
# Guernsey  St. Peter Port  49°26'N 02°33'W
# Guinea  Conakry 09°29'N 13°49'W
# Guinea-Bissau Bissau  11°45'N 15°45'W
# Guyana  Georgetown  06°50'N 58°12'W
# Haiti Port-au-Prince  18°40'N 72°20'W
# Heard Island and McDonald Islands   53°00'S 74°00'E
# Honduras  Tegucigalpa 14°05'N 87°14'W
# Hungary Budapest  47°29'N 19°05'E
# Iceland Reykjavik 64°10'N 21°57'W
# India New Delhi 28°37'N 77°13'E
# Indonesia Jakarta 06°09'S 106°49'E
# Iran (Islamic Republic of)  Tehran  35°44'N 51°30'E
# Iraq  Baghdad 33°20'N 44°30'E
# Ireland Dublin  53°21'N 06°15'W
# Israel  Jerusalem 31°47'N 35°12'E
# Italy Rome  41°54'N 12°29'E
# Jamaica Kingston  18°00'N 76°50'W
# Jordan  Amman 31°57'N 35°52'E
# Kazakhstan  Astana  51°10'N 71°30'E
# Kenya Nairobi 01°17'S 36°48'E
# Kiribati  Tarawa  01°30'N 173°00'E
# Kuwait  Kuwait  29°30'N 48°00'E
# Kyrgyzstan  Bishkek 42°54'N 74°46'E
# Lao People's Democratic Republic  Vientiane 17°58'N 102°36'E
# Latvia  Riga  56°53'N 24°08'E
# Lebanon Beirut  33°53'N 35°31'E
# Lesotho Maseru  29°18'S 27°30'E
# Liberia Monrovia  06°18'N 10°47'W
# Libyan Arab Jamahiriya  Tripoli 32°49'N 13°07'E
# Liechtenstein Vaduz 47°08'N 09°31'E
# Lithuania Vilnius 54°38'N 25°19'E
# Luxembourg  Luxembourg  49°37'N 06°09'E
# Macao, China  Macau 22°12'N 113°33'E
# Madagascar  Antananarivo  18°55'S 47°31'E
# Malawi  Lilongwe  14°00'S 33°48'E
# Malaysia  Kuala Lumpur  03°09'N 101°41'E
# Maldives  Male  04°00'N 73°28'E
# Mali  Bamako  12°34'N 07°55'W
# Malta Valletta  35°54'N 14°31'E
# Martinique  Fort-de-France  14°36'N 61°02'W
# Mauritania  Nouakchott  20°10'S 57°30'E
# Mayotte Mamoudzou 12°48'S 45°14'E
# Mexico  Mexico  19°20'N 99°10'W
# Micronesia (Federated States of)  Palikir 06°55'N 158°09'E
# Moldova, Republic of  Chisinau  47°02'N 28°50'E
# Mozambique  Maputo  25°58'S 32°32'E
# Myanmar Yangon  16°45'N 96°20'E
# Namibia Windhoek  22°35'S 17°04'E
# Nepal Kathmandu 27°45'N 85°20'E
# Netherlands Amsterdam/The Hague (seat of Gvnt)  52°23'N 04°54'E
# Netherlands Antilles  Willemstad  12°05'N 69°00'W
# New Caledonia Noumea  22°17'S 166°30'E
# New Zealand Wellington  41°19'S 174°46'E
# Nicaragua Managua 12°06'N 86°20'W
# Niger Niamey  13°27'N 02°06'E
# Nigeria Abuja 09°05'N 07°32'E
# Norfolk Island  Kingston  45°20'S 168°43'E
# Northern Mariana Islands  Saipan  15°12'N 145°45'E
# Norway  Oslo  59°55'N 10°45'E
# Oman  Masqat  23°37'N 58°36'E
# Pakistan  Islamabad 33°40'N 73°10'E
# Palau Koror 07°20'N 134°28'E
# Panama  Panama  09°00'N 79°25'W
# Papua New Guinea  Port Moresby  09°24'S 147°08'E
# Paraguay  Asuncion  25°10'S 57°30'W
# Peru  Lima  12°00'S 77°00'W
# Philippines Manila  14°40'N 121°03'E
# Poland  Warsaw  52°13'N 21°00'E
# Portugal  Lisbon  38°42'N 09°10'W
# Puerto Rico San Juan  18°28'N 66°07'W
# Qatar Doha  25°15'N 51°35'E
# Republic of Korea Seoul 37°31'N 126°58'E
# Romania Bucuresti 44°27'N 26°10'E
# Russian Federation  Moskva  55°45'N 37°35'E
# Rawanda Kigali  01°59'S 30°04'E
# Saint Kitts and Nevis Basseterre  17°17'N 62°43'W
# Saint Lucia Castries  14°02'N 60°58'W
# Saint Pierre and Miquelon Saint-Pierre  46°46'N 56°12'W
# Saint vincent and the Grenadines  Kingstown 13°10'N 61°10'W
# Samoa Apia  13°50'S 171°50'W
# San Marino  San Marino  43°55'N 12°30'E
# Sao Tome and Principe Sao Tome  00°10'N 06°39'E
# Saudi Arabia  Riyadh  24°41'N 46°42'E
# Senegal Dakar 14°34'N 17°29'W
# Sierra Leone  Freetown  08°30'N 13°17'W
# Slovakia  Bratislava  48°10'N 17°07'E
# Slovenia  Ljubljana 46°04'N 14°33'E
# Solomon Islands Honiara 09°27'S 159°57'E
# Somalia Mogadishu 02°02'N 45°25'E
# South Africa  Pretoria (adm.) / Cap Town (Legislative) / Bloemfontein (Judicial)  25°44'S 28°12'E
# Spain Madrid  40°25'N 03°45'W
# Sudan Khartoum  15°31'N 32°35'E
# Suriname  Paramaribo  05°50'N 55°10'W
# Swaziland Mbabane (Adm.)  26°18'S 31°06'E
# Sweden  Stockholm 59°20'N 18°03'E
# Switzerland Bern  46°57'N 07°28'E
# Syrian Arab Republic  Damascus  33°30'N 36°18'E
# Tajikistan  Dushanbe  38°33'N 68°48'E
# Thailand  Bangkok 13°45'N 100°35'E
# The Former Yugoslav Republic of Macedonia Skopje  42°01'N 21°26'E
# Togo  Lome  06°09'N 01°20'E
# Tonga Nuku'alofa  21°10'S 174°00'W
# Tunisia Tunis 36°50'N 10°11'E
# Turkey  Ankara  39°57'N 32°54'E
# Turkmenistan  Ashgabat  38°00'N 57°50'E
# Tuvalu  Funafuti  08°31'S 179°13'E
# Uganda  Kampala 00°20'N 32°30'E
# Ukraine Kiev (Rus)  50°30'N 30°28'E
# United Arab Emirates  Abu Dhabi 24°28'N 54°22'E
# United Kingdom of Great Britain and Northern Ireland  London  51°36'N 00°05'W
# United Republic of Tanzania Dodoma  06°08'S 35°45'E
# United States of America  Washington DC 39°91'N 77°02'W
# United States of Virgin Islands Charlotte Amalie  18°21'N 64°56'W
# Uruguay Montevideo  34°50'S 56°11'W
# Uzbekistan  Tashkent  41°20'N 69°10'E
# Vanuatu Port-Vila 17°45'S 168°18'E
# Venezuela Caracas 10°30'N 66°55'W
# Viet Nam  Hanoi 21°05'N 105°55'E
# Yugoslavia  Belgrade  44°50'N 20°37'E
# Zambia  Lusaka  15°28'S 28°16'E
# Zimbabwe  Harare  17°43'S 31°02'E
























DEFAULT_TSV_FILE            = 'instascrape.tsv'
DATUM_SPLIT_SIZE            = 18

IS_CREATED_COUNTRIES        = False
COUNTRIES_LIST              = []

IS_CREATED_CLUSTERS         = False
HAVERSINE_CLUSTERS          = {}

IS_CREATED_FILTERS_LIST     = False
FILTERS_LIST                = []

IS_CREATED_FILTERS_COUNT    = False
FILTERS_COUNT               = {}

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

# dat = fe.extract_from_tsv()
# vec = fe.filter_selection(dat,dat[0])
# vec = fe.filter_rarity(dat,dat[0])
# loc = fe.location_tagged_dataset(fe.extract_from_tsv())
# vec = fe.location_clustering_country(loc,loc[0])
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



# # 'location clustering' by country in which it is located

# def location_clustering_country(location_dataset, data_point):
#   ### Notes: perhaps add features based on country rarity?

#   # BEGIN_YOUR_CODE (around ??? lines of code expected)
#   def get_place(lat, lon):
#     """
#     Determine the country to which the latitude and
#     longitude belong to, or return None
#     """
#     url = "http://maps.googleapis.com/maps/api/geocode/json?"
#     url += "latlng=%s,%s&sensor=false" % (lat, lon)
#     v = urlopen(url).read()
#     j = json.loads(v)
#     components = j['results'][0]['address_components']
#     country = town = None
#     for c in components:
#         if "country" in c['types']:
#             country = c['long_name']
#         if "postal_town" in c['types']:
#             town = c['long_name']
#     #return town, country
#     print country
#     return str(country)

#   def create_total_countries_list(dataset):
#     countries_dict = Counter()
#     for datum in dataset:
#       latitude  = datum['location_latitude']
#       longitude = datum['location_longitude']

#       try:
#         country = get_place(latitude, longitude)
#       except IndexError:
#         country = "UNKNOWN"

#       countries_dict[country] += 1
#     countries_list = countries_dict.keys()
#     return sorted(countries_list)

#   global IS_CREATED_COUNTRIES
#   global COUNTRIES_LIST

#   if not IS_CREATED_COUNTRIES:
#     COUNTRIES_LIST = create_total_countries_list(location_dataset)
#     IS_CREATED_COUNTRIES = True

#   country_vector = [0] * OVERESTIMATE_COUNTRY_NUMBER
#   latitude  = data_point['location_latitude']
#   longitude = data_point['location_longitude']
#   country   = get_place(latitude, longitude)
#   country_vector[COUNTRIES_LIST.index(country)] = 1

#   # END_YOUR_CODE
  
#   return country_vector



# # 'location cluster' by haversine distance between lon/lat

# def location_clustering_distance(dataset, data_point, k_clusters=10):

#   # BEGIN_YOUR_CODE (around ??? lines of code expected)
#   def haversine(pt1,pt2):
#     """
#     Calculate the great circle distance between two points 
#     on the earth (specified in decimal degrees)
#     """
#     # convert decimal degrees to radians
#     lon1 = float(pt1['location_longitude'])
#     lat1 = float(pt1['location_latitude'])
#     lon2 = float(pt2['location_longitude'])
#     lat2 = float(pt2['location_latitude'])
#     lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
#     # haversine formula 
#     dlon = lon2 - lon1 
#     dlat = lat2 - lat1 
#     a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
#     c = 2 * math.asin(math.sqrt(a)) 
#     km = 6367 * c
#     return km 

#   def kmeans_cluster_by_distance(data, k_val): 
#     cluster_mapping = {}

#     centroids = random.sample(range(len(data)), k_val)
    
#     iters = 100
#     while iters > 0:
#       print iters
#       iters -= 1
#       clusters = dict()
#       for centroid in centroids:
#         #key = frozenset((float(centroid['location_longitude']),float(centroid['location_latitude'])))
#         #clusters[key] = set()
#         clusters[centroid] = []

#       print clusters.keys() ##################################################

#       for ind in range(len(data)):
#         if ind in centroids:
#           best_ind, best_dist = ind, 0
#         else:
#           best_ind, best_dist = 0, float("inf")
#           for centroid in centroids[1:]:
#             if haversine(data[ind], data[centroid]) < best_dist:
#               best_ind, best_dist = centroid, haversine(data[ind], data[centroid])
#         #key = frozenset((float(best_datum['location_longitude']),float(best_datum['location_latitude'])))
#         #print key
#         clusters[best_ind].append(ind)

#       new_centroids = []
#       for key, cluster in clusters.iteritems():
#         best_ind, best_dist = 0, float("inf")
#         for ind in cluster:
#           # lowest sum of distance
#           dist = sum([ haversine(data[ind], data[pt]) for pt in cluster ])
#           if dist < best_dist:
#             best_ind, best_dist = ind, dist
#         new_centroids.append(best_ind)

#       if sorted(new_centroids) == sorted(centroids):
#         break
#       else:
#         centroids = new_centroids

#     clusters_listified = [ list(clusters[key]) for key in clusters.keys() ]
#     clusters_listified = sorted(clusters_listified, key=len(points))
#     for i in xrange(k_val):
#       cluster_mapping[i] = clusters_listified[i]
#       print "Cluster "+str(i)+" has "+str(len(clusters_listified[i]))+" points."

#     return cluster_mapping
  
#   global IS_CREATED_CLUSTERS
#   global HAVERSINE_CLUSTERS

#   if not IS_CREATED_CLUSTERS:
#     HAVERSINE_CLUSTERS  = kmeans_cluster_by_distance(dataset, k_clusters)
#     IS_CREATED_CLUSTERS = True

#   cluster_vector = [0] * k_clusters
#   for key, points in HAVERSINE_CLUSTERS.items():
#     ind = dataset.index(data_point)
#     if ind in points:
#       cluster_vector[key] = 1
#       break

#   # END_YOUR_CODE
  
#   return cluster_vector



# 'filter selection' is a binary vector with filter choice toggled from precomputed alphabetical listing of filters from dataset

def filter_selection(dataset, data_point):
  global IS_CREATED_FILTERS_LIST
  global FILTERS_LIST  

  def alphabetical_filter_list(data):
    filters_set  = set()

    for datum in data:
      if datum['filter_type'] != None:
        filters_set.add(str(datum['filter_type']))
      else:
        filters_set.add("NONE")

    filters_list = list(filters_set)
    return sorted(filters_list)

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  if not IS_CREATED_FILTERS_LIST:
    FILTERS_LIST = alphabetical_filter_list(dataset)
    print FILTERS_LIST
    IS_CREATED_FILTERS_LIST = True

  select_vector = [0] * len(FILTERS_LIST)
  select_filter = data_point['filter_type']
  select_vector[FILTERS_LIST.index(str(select_filter))] = 1
  # END_YOUR_CODE
  
  return select_vector



def filter_rarity(dataset, data_point):
  global IS_CREATED_FILTERS_COUNT
  global FILTERS_COUNT 

  def filter_individual_counts(data):
    filters_count = Counter()

    for datum in data:
      if datum['filter_type'] != None:
        filters_count[datum['filter_type']] += 1
      else:
        filters_count["NONE"] += 1

    return filters_count         

  # BEGIN_YOUR_CODE (around ??? lines of code expected)
  if not IS_CREATED_FILTERS_COUNT:
    FILTERS_COUNT = filter_individual_counts(dataset)
    print FILTERS_COUNT
    IS_CREATED_FILTERS_COUNT = True

  rarity_vector = []
  rarity_value  = float(sum(FILTERS_COUNT.values())) / float(FILTERS_COUNT[data_point['filter_type']])
  rarity_vector.append(rarity_value)
  # END_YOUR_CODE
  
  return rarity_vector



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

  scores = { "Train Score": None,
             "K-Fold Dev Score": None,
             "Test Score": None }

  split_point = int(len(x_dataset)*split_proportion)

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

  scores["Train Score"]      = ml_func.score(X_train,Y_train)
  scores["Test Score"]       = ml_func.score(X_test,Y_test)
  scores["K-Fold Dev Score"] = None #TODO

  return scores



def auto_ablation_scoring_breakdown():
  return None



def multi_algorithm_mega_run():
  return None



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

#TODO: autorun style function for quick execution of location vs. no location, etc., does LinReg, DecTre, SVM with location vs. no location, graphs everything for easy comparison, and auto-ablation with selective feature creation, training/testing output scores

