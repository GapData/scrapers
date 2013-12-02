from scipy                 import stats
from sklearn               import svm
from sklearn               import linear_model
from urllib2               import urlopen
from collections           import Counter
from sklearn               import cross_validation
from sklearn.cluster       import KMeans
from sklearn.decomposition import PCA

import copy
import json
import math
import random
import numpy as np
import matplotlib.pyplot as plt



# Afghanistan Kabul !!!34.28.00+ 69.11.00+
# Albania Tirane  !!!41.18.00+ 19.49.00+
# Algeria Algiers !!!36.42.00+ 03.08.00+
# American Samoa  Pago Pago !!!14.16.00- 170.43.00-
# Andorra Andorra la Vella  !!!42.31.00+ 01.32.00+
# Angola  Luanda  !!!08.50.00- 13.15.00+
# Antigua and Barbuda W. Indies !!!17.20.00+ 61.48.00-
# Argentina Buenos Aires  !!!36.30.00- 60.00.00-
# Armenia Yerevan !!!40.10.00+ 44.31.00+
# Aruba Oranjestad  !!!12.32.00+ 70.02.00-
# Australia Canberra  !!!35.15.00- 149.08.00+
# Austria Vienna  !!!48.12.00+ 16.22.00+
# Azerbaijan  Baku  !!!40.29.00+ 49.56.00+
# Bahamas Nassau  !!!25.05.00+ 77.20.00-
# Bahrain Manama  !!!26.10.00+ 50.30.00+
# Bangladesh  Dhaka !!!23.43.00+ 90.26.00+
# Barbados  Bridgetown  !!!13.05.00+ 59.30.00-
# Belarus Minsk !!!53.52.00+ 27.30.00+
# Belgium Brussels  !!!50.51.00+ 04.21.00+
# Belize  Belmopan  !!!17.18.00+ 88.30.00-
# Benin Porto-Novo (constitutional cotonou) (seat of gvnt)  !!!06.23.00+ 02.42.00+
# Bhutan  Thimphu !!!27.31.00+ 89.45.00+
# Bolivia La Paz (adm.)/sucre (legislative) !!!16.20.00- 68.10.00-
# Bosnia and Herzegovina  Sarajevo  !!!43.52.00+ 18.26.00+
# Botswana  Gaborone  !!!24.45.00- 25.57.00+
# Brazil  Brasilia  !!!15.47.00- 47.55.00-
# British Virgin Islands  Road Town !!!18.27.00+ 64.37.00-
# Brunei Darussalam Bandar Seri Begawan !!!04.52.00+ 115.00.00+
# Bulgaria  Sofia !!!42.45.00+ 23.20.00+
# Burkina Faso  Ouagadougou !!!12.15.00+ 01.30.00-
# Burundi Bujumbura !!!03.16.00- 29.18.00+
# Cambodia  Phnom Penh  !!!11.33.00+ 104.55.00+
# Cameroon  Yaounde !!!03.50.00+ 11.35.00+
# Canada  Ottawa  !!!45.27.00+ 75.42.00-
# Cape Verde  Praia !!!15.02.00+ 23.34.00-
# Cayman Islands  George Town !!!19.20.00+ 81.24.00-
# Central African Republic  Bangui  !!!04.23.00+ 18.35.00+
# Chad  N'Djamena !!!12.10.00+ 14.59.00+
# Chile Santiago  !!!33.24.00- 70.40.00-
# China Beijing !!!39.55.00+ 116.20.00+
# Colombia  Bogota  !!!04.34.00+ 74.00.00-
# Comros  Moroni  !!!11.40.00- 43.16.00+
# Congo Brazzaville !!!04.09.00- 15.12.00+
# Costa Rica  San Jose  !!!09.55.00+ 84.02.00-
# Cote d'Ivoire Yamoussoukro  !!!06.49.00+ 05.17.00-
# Croatia Zagreb  !!!45.50.00+ 15.58.00+
# Cuba  Havana  !!!23.08.00+ 82.22.00-
# Cyprus  Nicosia !!!35.10.00+ 33.25.00+
# Czech Republic  Prague  !!!50.05.00+ 14.22.00+
# Democratic People's Republic of P'yongyang  !!!39.09.00+ 125.30.00+
# Democratic Republic of the Congo  Kinshasa  !!!04.20.00- 15.15.00+
# Denmark Copenhagen  !!!55.41.00+ 12.34.00+
# Djibouti  Djibouti  !!!11.08.00+ 42.20.00+
# Dominica  Roseau  !!!15.20.00+ 61.24.00-
# Dominica Republic Santo Domingo !!!18.30.00+ 69.59.00-
# East Timor  Dili  !!!08.29.00- 125.34.00+
# Ecuador Quito !!!00.15.00- 78.35.00-
# Egypt Cairo !!!30.01.00+ 31.14.00+
# El Salvador San Salvador  !!!13.40.00+ 89.10.00-
# Equatorial Guinea Malabo  !!!03.45.00+ 08.50.00+
# Eritrea Asmara  !!!15.19.00+ 38.55.00+
# Estonia Tallinn !!!59.22.00+ 24.48.00+
# Ethiopia  Addis Ababa !!!09.02.00+ 38.42.00+
# Falkland Islands (Malvinas) Stanley !!!51.40.00- 59.51.00-
# Faroe Islands Torshavn  !!!62.05.00+ 06.56.00-
# Fiji  Suva  !!!18.06.00- 178.30.00+
# Finland Helsinki  !!!60.15.00+ 25.03.00+
# France  Paris !!!48.50.00+ 02.20.00+
# French Guiana Cayenne !!!05.05.00+ 52.18.00-
# French Polynesia  Papeete !!!17.32.00- 149.34.00-
# Gabon Libreville  !!!00.25.00+ 09.26.00+
# Gambia  Banjul  !!!13.28.00+ 16.40.00-
# Georgia T'bilisi  !!!41.43.00+ 44.50.00+
# Germany Berlin  !!!52.30.00+ 13.25.00+
# Ghana Accra !!!05.35.00+ 00.06.00-
# Greece  Athens  !!!37.58.00+ 23.46.00+
# Greenland Nuuk  !!!64.10.00+ 51.35.00-
# Guadeloupe  Basse-Terre !!!16.00.00+ 61.44.00-
# Guatemala Guatemala !!!14.40.00+ 90.22.00-
# Guernsey  St. Peter Port  !!!49.26.00+ 02.33.00-
# Guinea  Conakry !!!09.29.00+ 13.49.00-
# Guinea-Bissau Bissau  !!!11.45.00+ 15.45.00-
# Guyana  Georgetown  !!!06.50.00+ 58.12.00-
# Haiti Port-au-Prince  !!!18.40.00+ 72.20.00-
# Heard Island and McDonald Islands   !!!53.00.00- 74.00.00+
# Honduras  Tegucigalpa !!!14.05.00+ 87.14.00-
# Hungary Budapest  !!!47.29.00+ 19.05.00+
# Iceland Reykjavik !!!64.10.00+ 21.57.00-
# India New Delhi !!!28.37.00+ 77.13.00+
# Indonesia Jakarta !!!06.09.00- 106.49.00+
# Iran (Islamic Republic of)  Tehran  !!!35.44.00+ 51.30.00+
# Iraq  Baghdad !!!33.20.00+ 44.30.00+
# Ireland Dublin  !!!53.21.00+ 06.15.00-
# Israel  Jerusalem !!!31.47.00+ 35.12.00+
# Italy Rome  !!!41.54.00+ 12.29.00+
# Jamaica Kingston  !!!18.00.00+ 76.50.00-
# Jordan  Amman !!!31.57.00+ 35.52.00+
# Kazakhstan  Astana  !!!51.10.00+ 71.30.00+
# Kenya Nairobi !!!01.17.00- 36.48.00+
# Kiribati  Tarawa  !!!01.30.00+ 173.00.00+
# Kuwait  Kuwait  !!!29.30.00+ 48.00.00+
# Kyrgyzstan  Bishkek !!!42.54.00+ 74.46.00+
# Lao People's Democratic Republic  Vientiane !!!17.58.00+ 102.36.00+
# Latvia  Riga  !!!56.53.00+ 24.08.00+
# Lebanon Beirut  !!!33.53.00+ 35.31.00+
# Lesotho Maseru  !!!29.18.00- 27.30.00+
# Liberia Monrovia  !!!06.18.00+ 10.47.00-
# Libyan Arab Jamahiriya  Tripoli !!!32.49.00+ 13.07.00+
# Liechtenstein Vaduz !!!47.08.00+ 09.31.00+
# Lithuania Vilnius !!!54.38.00+ 25.19.00+
# Luxembourg  Luxembourg  !!!49.37.00+ 06.09.00+
# Macao, China  Macau !!!22.12.00+ 113.33.00+
# Madagascar  Antananarivo  !!!18.55.00- 47.31.00+
# Malawi  Lilongwe  !!!14.00.00- 33.48.00+
# Malaysia  Kuala Lumpur  !!!03.09.00+ 101.41.00+
# Maldives  Male  !!!04.00.00+ 73.28.00+
# Mali  Bamako  !!!12.34.00+ 07.55.00-
# Malta Valletta  !!!35.54.00+ 14.31.00+
# Martinique  Fort-de-France  !!!14.36.00+ 61.02.00-
# Mauritania  Nouakchott  !!!20.10.00- 57.30.00+
# Mayotte Mamoudzou !!!12.48.00- 45.14.00+
# Mexico  Mexico  !!!19.20.00+ 99.10.00-
# Micronesia (Federated States of)  Palikir !!!06.55.00+ 158.09.00+
# Moldova, Republic of  Chisinau  !!!47.02.00+ 28.50.00+
# Mozambique  Maputo  !!!25.58.00- 32.32.00+
# Myanmar Yangon  !!!16.45.00+ 96.20.00+
# Namibia Windhoek  !!!22.35.00- 17.04.00+
# Nepal Kathmandu !!!27.45.00+ 85.20.00+
# Netherlands Amsterdam/The Hague (seat of Gvnt)  !!!52.23.00+ 04.54.00+
# Netherlands Antilles  Willemstad  !!!12.05.00+ 69.00.00-
# New Caledonia Noumea  !!!22.17.00- 166.30.00+
# New Zealand Wellington  !!!41.19.00- 174.46.00+
# Nicaragua Managua !!!12.06.00+ 86.20.00-
# Niger Niamey  !!!13.27.00+ 02.06.00+
# Nigeria Abuja !!!09.05.00+ 07.32.00+
# Norfolk Island  Kingston  !!!45.20.00- 168.43.00+
# Northern Mariana Islands  Saipan  !!!15.12.00+ 145.45.00+
# Norway  Oslo  !!!59.55.00+ 10.45.00+
# Oman  Masqat  !!!23.37.00+ 58.36.00+
# Pakistan  Islamabad !!!33.40.00+ 73.10.00+
# Palau Koror !!!07.20.00+ 134.28.00+
# Panama  Panama  !!!09.00.00+ 79.25.00-
# Papua New Guinea  Port Moresby  !!!09.24.00- 147.08.00+
# Paraguay  Asuncion  !!!25.10.00- 57.30.00-
# Peru  Lima  !!!12.00.00- 77.00.00-
# Philippines Manila  !!!14.40.00+ 121.03.00+
# Poland  Warsaw  !!!52.13.00+ 21.00.00+
# Portugal  Lisbon  !!!38.42.00+ 09.10.00-
# Puerto Rico San Juan  !!!18.28.00+ 66.07.00-
# Qatar Doha  !!!25.15.00+ 51.35.00+
# Republic of Korea Seoul !!!37.31.00+ 126.58.00+
# Romania Bucuresti !!!44.27.00+ 26.10.00+
# Russian Federation  Moskva  !!!55.45.00+ 37.35.00+
# Rawanda Kigali  !!!01.59.00- 30.04.00+
# Saint Kitts and Nevis Basseterre  !!!17.17.00+ 62.43.00-
# Saint Lucia Castries  !!!14.02.00+ 60.58.00-
# Saint Pierre and Miquelon Saint-Pierre  !!!46.46.00+ 56.12.00-
# Saint vincent and the Grenadines  Kingstown !!!13.10.00+ 61.10.00-
# Samoa Apia  !!!13.50.00- 171.50.00-
# San Marino  San Marino  !!!43.55.00+ 12.30.00+
# Sao Tome and Principe Sao Tome  !!!00.10.00+ 06.39.00+
# Saudi Arabia  Riyadh  !!!24.41.00+ 46.42.00+
# Senegal Dakar !!!14.34.00+ 17.29.00-
# Sierra Leone  Freetown  !!!08.30.00+ 13.17.00-
# Slovakia  Bratislava  !!!48.10.00+ 17.07.00+
# Slovenia  Ljubljana !!!46.04.00+ 14.33.00+
# Solomon Islands Honiara !!!09.27.00- 159.57.00+
# Somalia Mogadishu !!!02.02.00+ 45.25.00+
# South Africa  Pretoria (adm.) / Cap Town (Legislative) / Bloemfontein (Judicial)  !!!25.44.00- 28.12.00+
# Spain Madrid  !!!40.25.00+ 03.45.00-
# Sudan Khartoum  !!!15.31.00+ 32.35.00+
# Suriname  Paramaribo  !!!05.50.00+ 55.10.00-
# Swaziland Mbabane (Adm.)  !!!26.18.00- 31.06.00+
# Sweden  Stockholm !!!59.20.00+ 18.03.00+
# Switzerland Bern  !!!46.57.00+ 07.28.00+
# Syrian Arab Republic  Damascus  !!!33.30.00+ 36.18.00+
# Tajikistan  Dushanbe  !!!38.33.00+ 68.48.00+
# Thailand  Bangkok !!!13.45.00+ 100.35.00+
# The Former Yugoslav Republic of Macedonia Skopje  !!!42.01.00+ 21.26.00+
# Togo  Lome  !!!06.09.00+ 01.20.00+
# Tonga Nuku'alofa  !!!21.10.00- 174.00.00-
# Tunisia Tunis !!!36.50.00+ 10.11.00+
# Turkey  Ankara  !!!39.57.00+ 32.54.00+
# Turkmenistan  Ashgabat  !!!38.00.00+ 57.50.00+
# Tuvalu  Funafuti  !!!08.31.00- 179.13.00+
# Uganda  Kampala !!!00.20.00+ 32.30.00+
# Ukraine Kiev (Rus)  !!!50.30.00+ 30.28.00+
# United Arab Emirates  Abu Dhabi !!!24.28.00+ 54.22.00+
# United Kingdom of Great Britain and Northern Ireland  London  !!!51.36.00+ 00.05.00-
# United Republic of Tanzania Dodoma  !!!06.08.00- 35.45.00+
# United States of America  Washington DC !!!39.91.00+ 77.02.00-
# United States of Virgin Islands Charlotte Amalie  !!!18.21.00+ 64.56.00-
# Uruguay Montevideo  !!!34.50.00- 56.11.00-
# Uzbekistan  Tashkent  !!!41.20.00+ 69.10.00+
# Vanuatu Port-Vila !!!17.45.00- 168.18.00+
# Venezuela Caracas !!!10.30.00+ 66.55.00-
# Viet Nam  Hanoi !!!21.05.00+ 105.55.00+
# Yugoslavia  Belgrade  !!!44.50.00+ 20.37.00+
# Zambia  Lusaka  !!!15.28.00- 28.16.00+
# Zimbabwe  Harare  !!!17.43.00- 31.02.00+



DEFAULT_TSV_FILE         = 'instascrape.tsv'
DATUM_SPLIT_SIZE         = 18

IS_CREATED_CAPITAL_DICT  = False
CAPITAL_DICT             = {}

IS_CREATED_FILTERS_LIST  = False
FILTERS_LIST             = []

IS_CREATED_FILTERS_COUNT = False
FILTERS_COUNT            = {}

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

# QUICK RUN THROUGH GUIDE
# Basically, assuming the instascrape.tsv is in the same directory as this file, here's what you'd enter in a terminal:
#
# python
# import feature_extraction as fe
# data = fe.extract_from_tsv()
# location_data  = fe.location_tagged_dataset(data)
# x_data, y_data = fe.create_feature_vector(fe.extract_from_tsv()) # it's here where we input a list of feature extractors, right now it's a default if you see the definition below
# score = fe.apply_machine_learning_algorithm(x_data, y_data) 
# print score

# dat = fe.extract_from_tsv()
# vec = fe.filter_selection(dat,dat[0])
# vec = fe.filter_rarity(dat,dat[0])
# loc = fe.location_tagged_dataset(fe.extract_from_tsv())
# vec = fe.location_clustering_country(loc,loc[0])
# vec = fe.location_clustering_distance(loc,loc[0])

def extract_from_tsv(filename=DEFAULT_TSV_FILE, max_limit = None):
  '''
  Extracts information from scraped data file, returning
  a list of dicts corresponding to one image's worth of data.
  '''
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
  '''
  Returns a list of data (from the main dataset) that
  included latitude and longitude information.
  '''
  location_tagged_data = []

  for ind in xrange(len(dataset)):
    if dataset[ind]["location_longitude"] is not None and dataset[ind]["location_latitude"] is not None:
      location_tagged_data.append(copy.deepcopy(dataset[ind]))

  print "Total data points: " + str(len(location_tagged_data))
  return location_tagged_data



def basic_numerical_feature_extractor(data_point):
  '''
  Extracts data that is already numerical in nature.
  '''
  feature_vector     = []
  numerics_data_keys = ["image_comment_count","user_media_count","user_followed_by_count","user_follows_count"]

  for data_key in numerics_data_keys:
    feature_vector.append(data_point[data_key])

  return feature_vector



def sentiment_analysis():
  '''
  Analyzes textual data such as tags, captions, and comments to
  generate a feature vector.
  '''
  return None



def location_cluster_nearest_capital():
  '''
  Analyzes location dataset and creates a binary feature vector
  corresponding to each country's capital, assigning each data
  point to the capital is closest to by Haversine distance.
  '''
  def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees).
    '''
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km 

  # TODO: implement capital location clustering

  return None



def filter_selection(dataset, data_point):
  '''
  Analyzes filter type and creates a binary feature vector
  corresponding to the type of filter used on the Instagram.
  '''
  global IS_CREATED_FILTERS_LIST
  global FILTERS_LIST  

  def alphabetical_filter_list(data):
    '''
    Finds all filter types over dataset and creates
    ordered alphabetical listing of filter types.
    '''
    filters_set  = set()
    for datum in data:
      if datum['filter_type'] != None:
        filters_set.add(str(datum['filter_type']))
      else:
        filters_set.add("NONE")
    filters_list = list(filters_set)
    return sorted(filters_list)

  if not IS_CREATED_FILTERS_LIST:
    FILTERS_LIST = alphabetical_filter_list(dataset)
    print FILTERS_LIST
    IS_CREATED_FILTERS_LIST = True

  select_vector = [0] * len(FILTERS_LIST)
  select_filter = data_point['filter_type']
  select_vector[FILTERS_LIST.index(str(select_filter))] = 1
  
  return select_vector



def filter_rarity(dataset, data_point):
  '''
  Calculates "rarity" of an Instagram using a
  particular filter type, by dividing the total count
  of data over the count of a particular filter type.
  '''
  global IS_CREATED_FILTERS_COUNT
  global FILTERS_COUNT 

  def filter_individual_counts(data):
    '''
    Generates counts of each filter type used in
    Instagrams, including those who use none at all.
    '''
    filters_count = Counter()
    for datum in data:
      if datum['filter_type'] != None:
        filters_count[datum['filter_type']] += 1
      else:
        filters_count["NONE"] += 1
    return filters_count         

  if not IS_CREATED_FILTERS_COUNT:
    FILTERS_COUNT = filter_individual_counts(dataset)
    print FILTERS_COUNT
    IS_CREATED_FILTERS_COUNT = True

  rarity_vector = []
  rarity_value  = float(sum(FILTERS_COUNT.values())) / float(FILTERS_COUNT[data_point['filter_type']])
  rarity_vector.append(rarity_value)
  
  return rarity_vector



def image_relevancy():
  '''
  Generates a value corresponding to image relevancy, using data
  such as last comment time, image creation time, comment count,
  comment (time,text) tuples, followed by and likes counts.
  '''
  return None



def create_feature_vector(dataset, target_variable="likes_count", extractor_funcs=[basic_numerical_feature_extractor]):
  '''
  Applies all the specified feature extraction functions to input
  dataset, creating a complete feature vector to be fed into
  a supervised machine learning algorithm to predict target.
  '''
  x_data = []
  y_data = []

  for datum in dataset:
    x_datum = []

    for extractor_func in extractor_funcs:
      x_datum.append(extractor_func(datum))

    x_datum = [ sub_datum for sub_x_datum in x_datum for sub_datum in sub_x_datum ]
    x_data.append(x_datum)
    y_data.append(datum[target_variable])

  return (x_data,y_data)



def apply_machine_learning_algorithm(x_dataset, y_dataset, ml_func=linear_model.LinearRegression(), split_proportion=0.20, permute=False, k_folds=5, graph_pca=True):
  '''
  Applies an input machine learning algorithm to an x and y dataset,
  with optional custom inputs for handling split proportion, k-fold
  cross-validation, dataset permutation. Also graphs PCA-reduced data.
  '''
  def graph_pca_data(x_data, y_data, lower_lim=10, upper_lim=90):
    '''
    Reduces data using PCA, then graphs PCA-reduced data on x1 and x2
    axes, plotting target variable as an intensity-influenced color;
    data on the fringes of percentile scoring are discarded for clarity.
    '''
    pca_x_data = PCA(n_components=2).fit_transform(copy.deepcopy(x_data))

    x1_data = []
    x2_data = []
    y_minpt = min(y_data)
    y_maxpt = max(y_data)
    y_range = y_maxpt - y_minpt

    for pca_datum in pca_x_data:
      x1_data.append(pca_datum[0])
      x2_data.append(pca_datum[1])

    x1_arr = np.array(x1_data)
    x2_arr = np.array(x2_data)

    lower_x1 = stats.scoreatpercentile(x1_arr, lower_lim)
    upper_x1 = stats.scoreatpercentile(x1_arr, upper_lim)
    lower_x2 = stats.scoreatpercentile(x2_arr, lower_lim)
    upper_x2 = stats.scoreatpercentile(x2_arr, upper_lim)

    plt.hold(True)
    excluded = 0
    for ind in xrange(len(y_data)):
      print ind
      plt.hold(True)

      if x1_data[ind] < lower_x1 or x1_data[ind] > upper_x1 or x2_data[ind] < lower_x2 or x2_data[ind] > upper_x2:
        excluded += 1
      else:
        intensity = 0.20 + ((float(y_data[ind] - y_minpt) / float(y_range)) * 0.80)
        plt.plot(x1_data[ind], x2_data[ind], 'r.', alpha=intensity)
    print str(excluded) + " points excluded."

    plt.xlim(lower_x1,upper_x1)
    plt.ylim(lower_x2,upper_x2)
    plt.xlabel("PCA DIM ONE")
    plt.ylabel("PCA DIM TWO")
    plt.title("INTENSITY vs. PCA DIM [DARKER COLOR INDICATES HIGHER LIKE COUNT]")
    plt.show()

  scores = { "Train Score"     : None,
             "K-Fold Dev Score": None,
             "Test Score"      : None }

  split_point = int(len(x_dataset)*split_proportion)

  if graph_pca:
    graph_pca_data(x_dataset[0:25000], y_dataset[0:25000])

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

  k_scores = cross_validation.cross_val_score(ml_func, X_train, Y_train, cv=k_folds)

  scores["Train Score"]      = ml_func.score(X_train,Y_train)
  scores["K-Fold Dev Score"] = k_scores.mean()
  scores["Test Score"]       = ml_func.score(X_test,Y_test)

  return scores



def multi_algorithm_mega_run(x_dataset, y_dataset, ml_funcs, split_proportion=0.20, k_folds=5):
  '''
  Intended to run a lot of algorithms, on both permuted and 
  unpermuted data, location inclusive and exclusive data,
  to see which produces the best/most stable results under 
  general conditions. Good for making graphs too.
  '''
  # TODO: implement all run combinations

  # Linear Regression
  # Decision Tree
  # SVM
  return None



def auto_ablation_scoring_breakdown(dataset, extractor_funcs, ml_func, target_variable="likes_count", split_proportion=0.20, k_folds=5, permute=False):
  '''
  Intended to run one algorithm with very specific parameters,
  in order to analyze features individually and determine which
  features contribute how much improvement beyond our baseline.
  '''
  # TODO: implement ablative feature removal and feedback
  return None


