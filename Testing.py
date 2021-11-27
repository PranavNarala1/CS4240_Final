#This file will be used for testing purposes.

from Model import Model


#test_model = Model()
#test_model.train()
#test_model.save_model('test_model_trained_with_all_13_seasons')
#test_model.analyze_training()
#print(test_model.analyze_training())

test_model_trained_with_all_13_seasons = Model()
test_model_trained_with_all_13_seasons.load_model('test_model_trained_with_all_13_seasons')
print(test_model_trained_with_all_13_seasons.make_prediction('Warriors', 'Cavaliers', '2015-16'))