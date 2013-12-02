# ASSUMING feature_extraction.py is in same directory
import feature_extraction as fe

# IMPORT other necessities
from sklearn import linear_model

# GET entire dataset
data = fe.extract_from_tsv()

# GET location-inclusive dataset
location_data  = fe.location_tagged_dataset(data)

# GET feature vectors with supplied extraction functions
extraction_functions = [fe.basic_numerical_feature_extractor,
                        fe.filter_selection,
                        fe.filter_rarity]
x_data, y_data = fe.create_feature_vector(data, extractor_funcs=extraction_functions)

# VISUALIZE pca graph of dataset
fe.apply_machine_learning_algorithm(x_data, y_data)

# GET multiple run score data with supplied learning functions
learning_functions = [linear_model.LinearRegression()]
multiscores = fe.multi_algorithm_mega_run(x_data, y_data, learning_functions)

print "|======================================|"
print "Printing Multiple Scores:"
print multiscores
print "|======================================|"

# GET ablative score analysis by removing one feature at a time
extraction_functions = [fe.basic_numerical_feature_extractor,
                        fe.filter_selection,
                        fe.filter_rarity]
ablationscores = fe.auto_ablation_scoring_breakdown(data, extraction_funcs=extraction_functions)

print "|======================================|"
print "Printing Ablation Scores:"
print ablationscores
print "|======================================|"






