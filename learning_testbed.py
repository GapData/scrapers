# ASSUMING feature_extraction.py is in same directory
import feature_extraction as fe

# IMPORT other necessities
from sklearn import linear_model
from sklearn import tree
from sklearn import svm

# GET entire dataset
data = fe.extract_from_tsv()

# GET feature vectors with supplied extraction functions
extraction_functions = [fe.basic_numerical_feature_extractor,
                        fe.filter_selection,
                        fe.filter_rarity]
x_data, y_data = fe.create_feature_vector(data, extractor_funcs=extraction_functions)

# VISUALIZE pca graph of dataset
fe.apply_machine_learning_algorithm(x_data, y_data, graph_pca=True)

# TOGGLE pca preprocessing
print "|======================================|"
print "Printing w/ PCA PREPROCESS toggled off and on:"
print fe.apply_machine_learning_algorithm(x_data, y_data)
print fe.apply_machine_learning_algorithm(x_data, y_data, pca_preprocess=True)
print "|======================================|"

# INPUT pca dimensionality reduction
print "|======================================|"
print "Printing w/ PCA REDUCTION at normal and reduced dimension 2:"
print fe.apply_machine_learning_algorithm(x_data, y_data)
print fe.apply_machine_learning_algorithm(x_data, y_data, pca_reduction=2)
print "|======================================|"

# GET multiple run score data with supplied learning functions, target variable likes_count
learning_functions = [linear_model.LinearRegression(),
                      tree.DecisionTreeRegressor()]#,
                      #svm.SVR(C=1.0, epsilon=0.2)]
multiscores = fe.multi_algorithm_mega_run(x_data, y_data, learning_functions)

print "|======================================|"
print "Printing Multiple Scores (Target Variable: likes_count):"
print multiscores
print "|======================================|"

# GET multiple run score data with supplied learning functions, target variable likes_count/user_followed_by_count
learning_functions = [linear_model.LinearRegression(),
                      tree.DecisionTreeRegressor()]#,
                      #svm.SVR(C=1.0, epsilon=0.2)]
x_data, y_data = fe.create_feature_vector(data, target_variable="likes_normalized", extractor_funcs=extraction_functions)
multiscores = fe.multi_algorithm_mega_run(x_data, y_data, learning_functions)

print "|======================================|"
print "Printing Multiple Scores (Target Variable: likes_normalized):"
print multiscores
print "|======================================|"

# GET ablative score analysis by removing one feature at a time
extraction_functions = [fe.basic_numerical_feature_extractor,
                        fe.filter_selection,
                        fe.filter_rarity]
ablationscores = fe.auto_ablation_scoring_breakdown(data, extraction_funcs=extraction_functions, learn_func=tree.DecisionTreeRegressor(), permutation=True)

print "|======================================|"
print "Printing Ablation Scores:"
print ablationscores
print "|======================================|"

# GET location-inclusive dataset
location_data  = fe.location_tagged_dataset(data)

# TRY using location data with additional location feature extractor
extraction_functions = [fe.basic_numerical_feature_extractor,
                        fe.filter_selection,
                        fe.filter_rarity,
                        fe.location_cluster_nearest_capital]
loc_x_data, loc_y_data = fe.create_feature_vector(location_data, extractor_funcs=extraction_functions)

learning_functions = [linear_model.LinearRegression(),
                      tree.DecisionTreeRegressor()]#,
                      #svm.SVR(C=1.0, epsilon=0.2)]
multiscores = fe.multi_algorithm_mega_run(loc_x_data, loc_y_data, learning_functions)

print "|======================================|"
print "Printing Multiple Scores (w/ location-only data, i.e. 25% of dataset):"
print multiscores
print "|======================================|"

ablationscores = fe.auto_ablation_scoring_breakdown(location_data, extraction_funcs=extraction_functions, learn_func=tree.DecisionTreeRegressor(), permutation=True)

print "|======================================|"
print "Printing Ablation Scores (w/ location-only data, i.e. 25% of dataset):"
print ablationscores
print "|======================================|"


