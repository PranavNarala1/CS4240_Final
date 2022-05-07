# CS4240_Final

Made by Pranav Narala and Santosh Kandula

For our final project, we predicted the NBA playoff bracket for the 2007-2008, 2009-2010, 2012-2013, and 2015-2016 seasons. We used publicly available datasets on regular season data from past seasons to train a machine learning model. When testing the model, regular season data for the two teams in a series was input, and the output was the predicted team to win the series. The predicted team to win the series moved onto the next series, and this process was repeated to complete the predicted playoff bracket. Once we created the predicted playoff bracket, we compared it to the actual bracket from that year to evaluate how accurate the model is.

The code was written in python, and the project was developed on github. We used the tensorflow, sklearn, numpy, and pandas libraries during the project. The project code was broken into four python files, one python notebook, and csv files to store data on past seasons. One of the python files is a service class with functions made to get specific data from the csv files, and this file is called NBADataService. The other python file is called Model, and this has a class, called Model, that is be used to abstract a keras neural network. We also made classes that abstract a sklearn tree and a sklearn.ensemble random forest classifier calles TreeModel and RandomForestModel respectively. We decided to use the Model class because it had the greatest accuracy. The python notebook file is called Client, and it is functioning as the Driver program for the machine learning model. This is the file that is using a Model object, and the predictions and the evaluation of the predictions was done on this class.

A discovered side-effect of this model is that it can be used to predict winners of regular seasons games as well, but it will not take into consideration which team is the home team and which team is the away team.

Here are the project sources we got data from:

https://www.kaggle.com/druswick/nba-team-records-historic - nba_team_win.csv

https://www.kaggle.com/nathanlauga/nba-games?select=games.csv - 

https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2017-18&SeasonType=Regular%20Season - 

https://www.kaggle.com/mur418/nba-box-scores-19902020-regular-and-playoffs?select=2017-18_Regular_box_scores.csv - playoffs_box_score_data, regular_season_box_score_data


To use the model:

1. Download the files 
2. Import them in the program you are using them in.
3. Use the constructor Model() to create the model.
4. Use model_name.load_model('test_model_trained_with_all_13_seasons') to load a pretrained model.
5. Use model_name.make_prediction(team_1, team_2, year) to get a string containing the predicted team to win the series.

See documentation for more info.
