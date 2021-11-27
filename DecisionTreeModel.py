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
        return tree_prediction

    def save_model(self, file_path):
        joblib.dump(self.tree_model, file_path)

    def load_model(self, file_path):
        self.tree_model = joblib.load(file_path)
