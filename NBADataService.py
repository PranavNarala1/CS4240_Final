import pandas as pd
import numpy as np

#Data Year Range: (2005-06) to (2017-18)

#Account for team name changes (ex. Bobcats to Hornets)
abbreviation_to_name = {
'ATL'	: 'Atlanta Hawks',
'BOS'	: 'Boston Celtics',
'CHA'	: 'Charlotte Hornets',
'CHI'	: 'Chicago Bulls',
'CLE'	: 'Cleveland Cavaliers',
'DAL'	: 'Dallas Mavericks',
'DEN'	: 'Denver Nuggets',
'DET'	: 'Detroit Pistons',
'GSW'	: 'Golden State Warriors',
'HOU' : 'Houston Rockets',
'IND'	: 'Indiana Pacers',
'LAC' : 'Los Angeles Clippers',
'LAL'	: 'Los Angeles Lakers',
'MEM'	: 'Memphis Grizzlies',
'MIA'	: 'Miami Heat',
'MIL'	: 'Milwaukee Bucks',
'MIN'	: 'Minnesota Timberwolves',
'NOH'	: 'New Orleans Pelicans',
'NYK'	: 'New York Knicks',
'BKN'	: 'Brooklyn Nets',
'OKC'	: 'Oklahoma City Thunder',
'ORL'	: 'Orlando Magic',
'PHI'	: 'Philadelphia 76ers',
'PHO'	: 'Phoenix Suns',
'POR'	: 'Portland Trail Blazers',
'SAC'	: 'Sacramento Kings',
'TOR'	: 'Toronto Raptors',
'UTH'	: 'Utah Jazz',
'WAS'	: 'Washington Wizards'
}

def get_win_percentage(team_name, year):
    win_percentage_data = pd.read_csv('nba_team_win.csv')
    for row in win_percentage_data.iterrows():
        if row[1][1].lower() == team_name.lower() and row[1][0].lower() == year.lower():
            return row[1][3]

def get_offensive_rating(team_name, year):
    team_regular_season_data = pd.read_csv('nba_team_regular_season_offensive_and_defensive_ratings.csv')
    for row in team_regular_season_data.iterrows():
        if row[1][1].split()[-1].lower() == team_name.lower() and row[1][0] == year:
            return row[1][2]

def get_defensive_rating(team_name, year):
    team_regular_season_data = pd.read_csv('nba_team_regular_season_offensive_and_defensive_ratings.csv')
    for row in team_regular_season_data.iterrows():
        if row[1][1].split()[-1].lower() == team_name.lower() and row[1][0] == year:
            return row[1][3]

def to_team_name(abbreviation):
    return abbreviation_to_name[abbreviation]

def get_x_train():
    x_train_list = []
    for x in range(13):
        year = f'{2005 + x}-{str(2006 + x)[2:]}'
        year_data = pd.read_csv(fr'regular_season_box_score_data\{year}_Regular_box_scores.csv')
        for row in year_data.iterrows():
            #Prevents double addition of games into train_list
            if row[1][1].split()[1] == 'vs.':
                home_team = to_team_name(row[1][1].split()[0])
                away_team = to_team_name(row[1][1].split()[2])
                x_train_list.append([
                        get_win_percentage(home_team, year),
                        get_win_percentage(away_team, year),
                        get_offensive_rating(home_team, year),
                        get_offensive_rating(away_team, year),
                        get_defensive_rating(home_team, year),
                        get_defensive_rating(away_team, year)
                        ])

    print(x_train_list)
    return np.array(x_train_list)



def get_y_train():
    y_train_list = []
    for x in range(13):
        year = f'{2005 + x}-{str(2006 + x)[2:]}'
        year_data = pd.read_csv(fr'regular_season_box_score_data\{year}_Regular_box_scores.csv')
        for row in year_data.iterrows():
            #Prevents double addition of games into train_list
            if row[1][1].split()[1] == 'vs.':
                if row[1][3] == 'W':
                    y_train_list.append([
                        1
                    ])
                else:
                    y_train_list.append([
                        0
                    ])

    print(y_train_list)
    return np.array(y_train_list)

#Standardize data later so that offensive and defensive ratings are values from 0-1
def get_x_test(away_team, home_team, year):
    return [get_win_percentage(home_team, year), get_win_percentage(away_team, year),
            get_offensive_rating(home_team, year), get_offensive_rating(away_team, year),
            get_defensive_rating(home_team, year), get_defensive_rating(away_team, year)]

print(get_x_train())
print(get_y_train())
print(get_x_test('Spurs', 'Mavericks', '2009-10'))