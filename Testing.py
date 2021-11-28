#This file will be used for testing purposes.

#from Model import Model
#from DecisionTreeModel import DecisionTreeModel

from RandomForestModel import RandomForestModel

#test_tree_model = DecisionTreeModel()
#test_tree_model.train()
#test_tree_model.save_model('decision_tree_model')
#test_model.analyze_training()
#print(test_model.analyze_training())

#test_tree_model = DecisionTreeModel()
#test_tree_model.load_model('decision_tree_model')
#print(test_tree_model.make_prediction('Warriors', 'Cavaliers', '2015-16'))

#model = Model()
#model.load_model('test_model')
#print(model.test_model())

#test_tree_model = DecisionTreeModel()
#test_tree_model.load_model('decision_tree_model')
#print(test_tree_model.test_model())

random_forest_model = RandomForestModel()
random_forest_model.train()
random_forest_model.save_model('random_forest_model')