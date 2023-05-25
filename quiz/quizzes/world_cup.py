import pandas as pd
import numpy as np
df = pd.read_csv("quiz/data/wc/wc_detail.csv", usecols=['home_team', 'away_team', 'home_score', 'away_score','home_penalty', 'away_penalty', 'Date', 'Host', 'Year','home_red_card', 'away_red_card'])
df['home_red_card'] = df['home_red_card'].replace([np.nan, np.inf], '').str.count('·').fillna(0).astype(int)
df['away_red_card'] = df['away_red_card'].replace([np.nan, np.inf], '').str.count('·').fillna(0).astype(int)

def apperance(answer):
    home_match = df['home_team'].value_counts()
    away_match = df['away_team'].value_counts()
    total_match = home_match.add(away_match).sort_values(ascending=False)
    if answer[1] not in total_match:
        return 0
    else:
        if total_match.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score = len(total_match) - total_match.index.get_loc(answer[1])
        return score

def score_goal(answer):
    home_scores = df.groupby('home_team')['home_score'].sum()
    away_scores = df.groupby('away_team')['away_score'].sum()
    total_scores = home_scores.add(away_scores, fill_value=0).sort_values(ascending=False)
    if answer[1] not in total_scores:
        return 0
    else:
        if total_scores.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score = len(total_scores) - total_scores.index.get_loc(answer[1])
        return score

def penalty_goal(answer):
    home_penalty = df.groupby('home_team')['home_penalty'].sum()
    away_penalty = df.groupby('away_team')['away_penalty'].sum()
    total_penalty = home_penalty.add(away_penalty, fill_value=0).sort_values(ascending=False)
    if answer[1] not in total_penalty:
        return 0
    else:
        if total_penalty.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score = len(total_penalty) - total_penalty.index.get_loc(answer[1])
        return score
    
def conceded_goal(answer):
    home_conceded = df.groupby('home_team')['away_score'].sum()
    away_conceded = df.groupby('away_team')['home_score'].sum()
    total_conceded = home_conceded.add(away_conceded, fill_value=0).sort_values(ascending=False)
    if answer[1] not in total_conceded:
        return 0
    else:
        if total_conceded.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score = len(total_conceded) - total_conceded.index.get_loc(answer[1])
        return score
    
def most_red(answer):
    home_red = df.groupby('home_team')['home_red_card'].sum()
    away_red = df.groupby('away_team')['away_red_card'].sum()
    total_card = home_red.add(away_red, fill_value=0).sort_values(ascending=False)
    if answer[1] not in total_card:
        return total_card
    else:
        if total_card.index.get_loc(answer[1]) > 30:
            score = 0
        else:
            score = len(total_card) - total_card.index.get_loc(answer[1])
        return score

    
def goal_to_apperance(answer): 
    home_goals = df.groupby('home_team')['home_score'].sum()
    away_goals = df.groupby('away_team')['away_score'].sum()
    total_goals = home_goals.add(away_goals, fill_value=0)
    
    matches_played = df['home_team'].value_counts() + df['away_team'].value_counts()
    goal_apperance = total_goals.divide(matches_played).sort_values(ascending=False)
    if answer[1] not in goal_apperance:
        return 0
    else:
        if goal_apperance.index.get_loc(answer[1])>30:
            score=0
        else:
            score = len(goal_apperance) - goal_apperance.index.get_loc(answer[1])
        return score

functions=[apperance, score_goal, penalty_goal, conceded_goal, most_red, goal_to_apperance]
questions = ['Most apperance', 'Most Goals', 'Most Penalty Scored', 'Most conceded goal', 'Most Red card', 'Most Goal/Apperance']