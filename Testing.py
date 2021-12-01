#This file will be used for testing purposes.

from Model import Model
#from RandomForestModel import RandomForestModel
#from DecisionTreeModel import DecisionTreeModel
import NBADataService
import numpy as np


print(type(NBADataService.get_x_test('Heat', 'Lakers', '2008-09')))

#print(type(NBADataService.to_team_name('CHA', '2013-14')))

#test_tree_model = DecisionTreeModel()
#test_tree_model.train()
#test_tree_model.save_model('decision_tree_model')
#test_model.analyze_training()
#print(test_model.analyze_training())

#test_tree_model = DecisionTreeModel()
#test_tree_model.load_model('decision_tree_model')
#print(test_tree_model.make_prediction('Warriors', 'Cavaliers', '2015-16'))

#model = Model()
#model.load_model('test_model_trained_with_all_13_seasons')

#print(model.make_prediction('Pacers', 'Heat', '2012-13'))

#model.load_model('test_model_trained_with_all_13_seasons')

#print(model.test_model())

#test_tree_model = DecisionTreeModel()
#test_tree_model.load_model('decision_tree_model')
#print(test_tree_model.test_model())

#random_forest_model = RandomForestModel()
#random_forest_model.train()
#random_forest_model.save_model('random_forest_model')

#random_forest_model = RandomForestModel()
#random_forest_model.load_model('random_forest_model')
#print(random_forest_model.test_model())