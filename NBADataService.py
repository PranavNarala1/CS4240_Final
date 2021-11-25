import pandas as pd

def get_win_percentage(team_name, year):
    win_percentage_data = pd.read_csv('nba_team_win.csv')
    for row in win_percentage_data.iterrows():
        if row[1][1].lower() == team_name.lower() and row[1][0].lower() == year.lower():
            return row[1][3]