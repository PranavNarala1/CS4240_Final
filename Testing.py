#This file will be used for testing purposes.

#from Model import Model
from DecisionTreeModel import DecisionTreeModel

test_tree_model = DecisionTreeModel()
test_tree_model.train()
test_tree_model.save_model('decision_tree_model')
#test_model.analyze_training()
#print(test_model.analyze_training())

#test_model_trained_with_all_13_seasons = Model()
#test_model_trained_with_all_13_seasons.load_model('test_model_trained_with_all_13_seasons')
#print(test_model_trained_with_all_13_seasons.make_prediction('Warriors', 'Cavaliers', '2015-16'))