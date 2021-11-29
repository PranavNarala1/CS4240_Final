import NBADataService
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib

class RandomForestModel(object):

    def __init__(self):
        self.random_forest_model = RandomForestClassifier(n_estimators=250)

    def train(self):
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.random_forest_model.fit(x_train, y_train)

    def make_prediction(self, team_1, team_2, year):
        x_test = NBADataService.get_x_test(team_1, team_2, year)
        random_forest_prediction = self.random_forest_model.predict(x_test)
        if random_forest_prediction == 1:
            return f'The predicted winner is: {team_2}'
        else:
            return f'The predicted winner is: {team_1}'

    def save_model(self, file_path):
        joblib.dump(self.random_forest_model, file_path)

    def load_model(self, file_path):
        self.random_forest_model = joblib.load(file_path)

    def test_model(self):
        x_test = NBADataService.get_x_test_playoffs()
        y_test = NBADataService.get_y_test_playoffs()
        random_forest_predictions = self.random_forest_model.predict(x_test)
        return metrics.accuracy_score(y_test, random_forest_predictions)
