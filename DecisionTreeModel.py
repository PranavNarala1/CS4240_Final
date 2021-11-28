import NBADataService
from sklearn import tree
import joblib

class DecisionTreeModel(object):

    def __init__(self):
        self.tree_model = tree.DecisionTreeClassifier()

    def train(self):
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.tree_model = self.tree_model.fit(x_train, y_train)

    def make_prediction(self, team_1, team_2, year):
        x_test = NBADataService.get_x_test(team_1, team_2, year)
        tree_prediction = self.tree_model.predict(x_test)
        if tree_prediction == 1:
            return f'The predicted winner is: {team_2}'
        else:
            return f'The predicted winner is: {team_1}'


    def save_model(self, file_path):
        joblib.dump(self.tree_model, file_path)

    def load_model(self, file_path):
        self.tree_model = joblib.load(file_path)

    def test_model(self):
        x_test = NBADataService.get_x_test_playoffs()
        y_test = NBADataService.get_y_test_playoffs()
        return self.tree_model.score(x_test, y_test)
