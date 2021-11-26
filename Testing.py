#This file will be used for testing purposes.

from Model import Model

#print(NBADataService.get_offensive_rating("Mavericks", "2011-12"))
#print(NBADataService.get_defensive_rating("Nuggets", "2009-10"))

test_model = Model()
test_model.train()
test_model.save_model('test_model')
test_model.analyze_training()
print(test_model.analyze_training())

#test_model = Model()
#test_model.load_model('test_model')
#print(test_model.make_prediction('Nuggets', 'Lakers', '2007-08'))