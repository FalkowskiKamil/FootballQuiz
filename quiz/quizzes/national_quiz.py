import pandas as pd
from .calculator import calculate_score
df = pd.read_csv("quiz/data/national/results.csv", encoding="ISO-8859-1")
df2 = pd.read_csv("quiz/data/national/goalscorers.csv", encoding="ISO-8859-1")

def info():
    nations = df['home_team'].sort_values().unique
    date = df['date'].sort_values()
    competition =  df['tournament'].unique()
    question = ['Most Goal', 'Most Home Goal', 'Most Away Goal',\
                "Most Own Goal", 'Most World Cup', 'Most Penalty Scored']
    return [nations, date[0], date.iloc[-1], competition, question]

def home_goal(answer):
    home_team = df.groupby('home_team')
    rank_table=home_team['home_score'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table)

def away_goal(answer):
    away_team = df.groupby('away_team')
    rank_table = away_team['away_score'].count().sort_values(ascending=False) 
    return calculate_score(answer[1], rank_table)

def most_goal(answer):
    most_goal=df2.groupby('team')
    rank_table = most_goal['team'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table)

def most_own_goal(answer):
    rank_table = df2[df2['own_goal'] == True].groupby('team')['own_goal'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table)

def most_wc_goal(answer):
    world_cup_data = df[df['tournament'] == 'FIFA World Cup']
    score_totals = world_cup_data.groupby('country')['home_score', 'away_score'].sum()
    rank_table = score_totals['home_score'] + score_totals['away_score']
    return calculate_score(answer[1], rank_table)

def most_penalty_goal(answer):
    rank_table = df2[df2['penalty'] == True].groupby('team')['penalty'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table)

national_functions = [most_goal, home_goal, away_goal, most_own_goal, most_wc_goal, most_penalty_goal]

def result(items):
    score=0
    for i, answer in enumerate(items):
        if i < len(national_functions):
            score += national_functions[i](answer)
    return score