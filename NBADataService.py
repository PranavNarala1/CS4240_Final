import pandas as pd
import numpy as np

#Data Year Range: (2005-06) to (2017-18)

def get_win_percentage(team_name, year):
    win_percentage_data = pd.read_csv('nba_team_win.csv')
    for row in win_percentage_data.iterrows():
        if row[1][1].lower() == team_name.lower() and row[1][0].lower() == year.lower():
            return row[1][3]

def get_offensive_rating(team_name, year):
    team_regular_season_data = pd.read_csv('NBA_Team_Stats_Regular_Season.csv')
    for row in team_regular_season_data.iterrows():
        if row[1][1].split()[-1].lower() == team_name.lower() and row[1][0] == year:
            return row[1][6]

def get_defensive_rating(team_name, year):
    team_regular_season_data = pd.read_csv('NBA_Team_Stats_Regular_Season.csv')
    for row in team_regular_season_data.iterrows():
        if row[1][1].split()[-1].lower() == team_name.lower() and row[1][0] == year:
            return row[1][7]

def get_x_train():
    pass

def get_y_train():
    pass

def get_x_test(away_team, home_team, year):
    return [get_win_percentage(home_team, year), get_win_percentage(away_team, year),
            get_offensive_rating(home_team, year), get_offensive_rating(away_team, year),
            get_defensive_rating(home_team, year), get_defensive_rating(away_team, year)]