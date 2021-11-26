#This file will be used for testing purposes.

from Model import Model

#print(NBADataService.get_offensive_rating("Mavericks", "2011-12"))
#print(NBADataService.get_defensive_rating("Nuggets", "2009-10"))

#test_model = Model()
#test_model.train()
#test_model.save_model('test_model_trained_with_all_13_seasons')
#test_model.analyze_training()
#print(test_model.analyze_training())

test_model_trained_with_all_13_seasons = Model()
test_model_trained_with_all_13_seasons.load_model('test_model_trained_with_all_13_seasons')
print(test_model_trained_with_all_13_seasons.make_prediction('Celtics', 'Grizzlies', '2007-08'))
print(test_model_trained_with_all_13_seasons.make_prediction('Grizzlies', 'Celtics', '2007-08'))


#with open('x_train_data', 'r') as x_train_data:
#    print(len(x_train_data.readlines()))