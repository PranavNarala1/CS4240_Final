#This class will be used for testing purposes.

import Model
import NBADataService

#print(NBADataService.get_offensive_rating("Mavericks", "2011-12"))
#print(NBADataService.get_defensive_rating("Nuggets", "2009-10"))

test_model = Model()
test_model.train()
test_model.analyze_training()
test_model.save('test_model')