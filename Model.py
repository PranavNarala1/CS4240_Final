import tensorflow as tf
from tensorflow import keras
import numpy as np
import NBADataService
import pandas as pd

class Model(object):

    def __init__(self):
        self.model = keras.models.Sequential([
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(25, activation="swish"),
            keras.layers.Dense(1, activation="sigmoid")
        ])
        self.model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")

    def train(self, epochs=10):
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.history = self.model.fit(x_train, y_train, epochs)

    def analyze_training(self):
        pd.DataFrame(self.history.history).plot(figsize=(16, 10))

    #Fix make_prediction
    def make_prediction(self, team_1, team_2, year):
        #Make sure that the home_team and away_team formatting with the model is consistent.
        x_test_1 = NBADataService.get_x_test(team_1, team_2, year)
        x_test_2 = NBADataService.get_x_test(team_2, team_1, year)
        prediction = (x_test_1 + x_test_2) / 2.0
        return f"{home_team} has a {prediction * 100}% chance of winning"

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = keras.models.load_model(file_path)
