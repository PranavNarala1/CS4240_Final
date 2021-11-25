# CS4240_Final

For our final project, we are going to predict the NBA playoff bracket for the 2007-2008, 2009-2010, 2012-2013, and 2015-2016 seasons. We will use publicly available datasets on past seasons to train a machine learning model. When testing the model, regular season data for the two teams in a series will be the input for the models, and the output will be the predicted team to win the series. The predicted team to win the series will move onto the next series, and this process will be repeated to complete the predicted playoff bracket. Once we create the predicted playoff bracket, we will compare it to the actual bracket from that year to evaluate how accurate the model is.

This code will be written in python, and the project will be on github. We are planning to use libraries such as tensorflow, numpy, and pandas during the project. The project code will be broken into two python files, one python notebook, and csv files to store data on past seasons. One of the python files will be a service class with functions made to get specific data from the csv files, and this file will be called NBADataService. The other python file will be called Model, and this will have a class, called Model, that will be used to abstract our machine learning model. The python notebook file will be called Client, and it will function as the Driver program for the machine learning model. This is the file that will use a Model object, and the predictions and the evaluation of the predictions will be done on this class.
