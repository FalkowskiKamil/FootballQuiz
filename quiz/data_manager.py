import pandas as pd
df = pd.read_csv("quiz/data/national/results.csv", encoding="ISO-8859-1")

def get_info(type):
    if type == 'nation':
        return df['home_team'].unique
    
def home_goal(answer):
    home_team = df.groupby('home_team')
    home_scores=home_team['home_score'].count().sort_values(ascending=False)
    if home_scores.index.get_loc(answer) > 30:
        score=0
    else:
        score=len(home_scores) - home_scores.index.get_loc(answer)
    return score

def away_goal(answer):
    away_team = df.groupby('away_team')
    away_scores = away_team['away_score'].count().sort_values(ascending=False) 
    if away_scores.index.get_loc(answer) > 30:
        score=0
    else:
        score=len(away_scores) - away_scores.index.get_loc(answer)
    return score

def most_goal(answer):
    most_goal=df.groupby('home_team')['home_score'].count().sort_values(ascending=False) \
    + df.groupby('away_team')['away_score'].count().sort_values(ascending=False) 
    if most_goal.index.get_loc(answer) > 30:
        score=0
    else:
        score=len(most_goal) - most_goal.index.get_loc(answer)
    return score

def most_own_goal(answer):
    return

def most_wc_goal(answer):
    return

def most_penalty_goal(answer):
    return 