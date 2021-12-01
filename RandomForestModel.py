import NBADataService
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib

"""
RandomForestModel is a class that abstracts a sklearn RandomForestClassifier.
"""
class RandomForestModel(object):

    def __init__(self):
        """
        Constructor for RandomForestModel that initializes the sklearn random forest classifier it abstracts.
        """
        self.random_forest_model = RandomForestClassifier(n_estimators=250)

    def train(self):
        """
        Trains the random forest classifier it abstracts.
        """
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.random_forest_model.fit(x_train, y_train)

    def make_prediction(self, team_1, team_2, year):
        """
        Returns a string with the predicted winner.

        :param team_1: one of the teams playing
        :param team_2: the other team playing
        :param year: the season they are playing
        :return: the predicted winner
        :rtype: str
        """
        x_test = NBADataService.get_x_test(team_1, team_2, year)
        random_forest_prediction = self.random_forest_model.predict(x_test)
        if random_forest_prediction == 1:
            return f'The predicted winner is: {team_2}'
        else:
            return f'The predicted winner is: {team_1}'

    def save_model(self, file_path):
        """
        Saves the model at file_path.

        :param file_path: the path where the file will be saved
        """
        joblib.dump(self.random_forest_model, file_path)

    def load_model(self, file_path):
        """
        Loads the model at file_path.

        :param file_path: the path where the model will be loaded from
        """
        self.random_forest_model = joblib.load(file_path)

    def test_model(self):
        """
        Tests the accuracy of the model using playoff data from the 2007-2008, 2009-2010, 2012-2013, and 2015-2016
        seasons.
        """
        x_test = NBADataService.get_x_test_playoffs()
        y_test = NBADataService.get_y_test_playoffs()
        random_forest_predictions = self.random_forest_model.predict(x_test)
        return metrics.accuracy_score(y_test, random_forest_predictions)
