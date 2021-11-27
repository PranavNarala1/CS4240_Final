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

    def train(self):
        x_train = NBADataService.get_x_train()
        y_train = NBADataService.get_y_train()
        self.history = self.model.fit(x_train, y_train, epochs=10)

    def analyze_training(self):
        pd.DataFrame(self.history.history).plot(figsize=(16, 10))

    def make_prediction(self, team_1, team_2, year):
        x_test = NBADataService.get_x_test(team_1, team_2, year)
        team_2_output = self.model.predict(x_test)[0][0]
        x_test = NBADataService.get_x_test(team_2, team_1, year)
        team_1_output = self.model.predict(x_test)[0][0]
        if team_2_output > team_1_output:
            return team_2
        else:
            return team_1

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = keras.models.load_model(file_path)
