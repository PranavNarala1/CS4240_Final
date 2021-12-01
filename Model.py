import tensorflow as tf
from tensorflow import keras
import numpy as np
import NBADataService
import pandas as pd

"""
Model is a class that abstracts a keras neural network.
"""
class Model(object):

    def __init__(self):
        """
        Constructor for Model that initializes the keras neural network it abstracts.
        """
        self.model = keras.models.Sequential([
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(1, activation="sigmoid")
        ])
        self.model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")

    def train(self):
        """
        Trains the neural network it abstracts.
        """
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.history = self.model.fit(x_train, y_train, epochs=10)

    def analyze_training(self):
        """
        Displays information about the training of the model.
        """
        pd.DataFrame(self.history.history).plot(figsize=(16, 10))

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
        team_2_output = self.model.predict(x_test)[0][0]
        x_test = NBADataService.get_x_test(team_2, team_1, year)
        team_1_output = self.model.predict(x_test)[0][0]
        if team_2_output > team_1_output:
            return f'The predicted winner is: {team_2}'
        else:
            return f'The predicted winner is: {team_1}'

    def save_model(self, file_path):
        """
        Saves the model at file_path.

        :param file_path: the path where the file will be saved
        """
        self.model.save(file_path)

    def load_model(self, file_path):
        """
        Loads the model at file_path.

        :param file_path: the path where the model will be loaded from
        """
        self.model = keras.models.load_model(file_path)

    def test_model(self):
        """
        Tests the accuracy of the model using playoff data from the 2007-2008, 2009-2010, 2012-2013, and 2015-2016
        seasons.
        """
        x_test = NBADataService.get_x_test_playoffs()
        y_test = NBADataService.get_y_test_playoffs()
        return self.model.evaluate(x_test, y_test)
