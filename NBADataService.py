import pandas as pd
import numpy as np

#Data Year Range: (2005-06) to (2017-18)

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
'HOU'   : 'Houston Rockets',
'IND'	: 'Indiana Pacers',
'LAC'   : 'Los Angeles Clippers',
'LAL'	: 'Los Angeles Lakers',
'MEM'	: 'Memphis Grizzlies',
'MIA'	: 'Miami Heat',
'MIL'	: 'Milwaukee Bucks',
'MIN'	: 'Minnesota Timberwolves',
'NJN'   : 'New Jersey Nets',
'NOH'   : 'New Orleans Hornets',
'NOK'   : 'New Orleans/Oklahoma City Hornets',
'NOP'	: 'New Orleans Pelicans',
'NYK'	: 'New York Knicks',
'BKN'	: 'Brooklyn Nets',
'OKC'	: 'Oklahoma City Thunder',
'ORL'	: 'Orlando Magic',
'PHI'	: 'Philadelphia 76ers',
'PHX'	: 'Phoenix Suns',
'POR'	: 'Portland Trail Blazers',
'SAC'	: 'Sacramento Kings',
'SAS'   : 'San Antonio Spurs',
'SEA'   : 'Seattle Supersonics',
'TOR'	: 'Toronto Raptors',
'UTA'	: 'Utah Jazz',
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

def to_team_name(abbreviation, year):
    if (year == '2013-14' or int(year[5:]) <= 13) and abbreviation == 'CHA':
        return "Bobcats"
    else:
        return abbreviation_to_name[abbreviation].split()[-1]

def get_x_train():
    x_train_list = []
    for x in range(13):
        year = f'{2005 + x}-{str(2006 + x)[2:]}'
        year_data = pd.read_csv(fr'regular_season_box_score_data\{year}_Regular_box_scores.csv')
        for row in year_data.iterrows():
            team_2 = to_team_name(row[1][0].split()[0], year)
            team_1 = to_team_name(row[1][0].split()[2], year)
            x_train_list.append([
                    get_win_percentage(team_2, year),
                    get_win_percentage(team_1, year),
                    get_offensive_rating(team_2, year) / 120,
                    get_offensive_rating(team_1, year) / 120,
                    get_defensive_rating(team_2, year) / 120,
                    get_defensive_rating(team_1, year) / 120
                    ])
    return np.asarray(x_train_list).astype(np.float32)



def get_y_train():
    y_train_list = []
    for x in range(13):
        year = f'{2005 + x}-{str(2006 + x)[2:]}'
        year_data = pd.read_csv(fr'regular_season_box_score_data\{year}_Regular_box_scores.csv')
        for row in year_data.iterrows():
            if row[1][1] == 'W':
                y_train_list.append(1)
            else:
                y_train_list.append(0)
    return np.asarray(y_train_list).astype(np.int64)

def get_x_test(team_1, team_2, year):
    return [[get_win_percentage(team_2, year), get_win_percentage(team_1, year),
            get_offensive_rating(team_2, year), get_offensive_rating(team_1, year),
            get_defensive_rating(team_2, year), get_defensive_rating(team_1, year)]]

def get_x_test_playoffs():
    x_test_list = []
    for x in ['2007-08', '2009-10', '2012-13', '2015-16']:
        year = x
        year_data = pd.read_csv(fr'playoffs_box_score_data\{year}_Playoffs_box_scores.csv')
        for row in year_data.iterrows():
            team_2 = to_team_name(row[1][0].split()[0], year)
            team_1 = to_team_name(row[1][0].split()[2], year)
            x_test_list.append([
                get_win_percentage(team_2, year),
                get_win_percentage(team_1, year),
                get_offensive_rating(team_2, year) / 120,
                get_offensive_rating(team_1, year) / 120,
                get_defensive_rating(team_2, year) / 120,
                get_defensive_rating(team_1, year) / 120
            ])
    return np.asarray(x_test_list).astype(np.float32)

def get_y_test_playoffs():
    y_test_list = []
    for x in ['2007-08', '2009-10', '2012-13', '2015-16']:
        year = x
        year_data = pd.read_csv(fr'playoffs_box_score_data\{year}_Playoffs_box_scores.csv')
        for row in year_data.iterrows():
            if row[1][1] == 'W':
                y_test_list.append(1)
            else:
                y_test_list.append(0)
    return np.asarray(y_test_list).astype(np.int64)
