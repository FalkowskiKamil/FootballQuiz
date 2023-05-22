import pandas as pd
df = pd.read_csv("quiz/data/national/results.csv", encoding="ISO-8859-1")
df2 = pd.read_csv("quiz/data/national/goalscorers.csv", encoding="ISO-8859-1")

def home_goal(answer):
    home_team = df.groupby('home_team')
    home_scores=home_team['home_score'].count().sort_values(ascending=False)
    if answer[1] not in home_scores:
        return 0
    else:
        if home_scores.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score=len(home_scores) - home_scores.index.get_loc(answer[1])
        return score

def away_goal(answer):
    away_team = df.groupby('away_team')
    away_scores = away_team['away_score'].count().sort_values(ascending=False) 
    if answer[1] not in away_scores:
        return 0
    else:
        if away_scores.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score=len(away_scores) - away_scores.index.get_loc(answer[1])
        return score

def most_goal(answer):
    most_goal=df2.groupby('team')
    most_goal = most_goal['team'].count().sort_values(ascending=False)
    if answer[1] not in most_goal:
        return 0
    else:
        if most_goal.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score=len(most_goal) - most_goal.index.get_loc(answer[1])
        return score

def most_own_goal(answer):
    own_goal_counts = df2[df2['own_goal'] == True].groupby('team')['own_goal'].count().sort_values(ascending=False)
    if answer[1] not in own_goal_counts:
        return 0
    else:
        if own_goal_counts.index.get_loc(answer[1]) > 10:
            score=0
        else:
            score = len(own_goal_counts) - own_goal_counts.index.get_loc(answer[1])
        return score

def most_wc_goal(answer):
    world_cup_data = df[df['tournament'] == 'FIFA World Cup']
    score_totals = world_cup_data.groupby('country')['home_score', 'away_score'].sum()
    score_totals['total_score'] = score_totals['home_score'] + score_totals['away_score']
    if answer[1] not in score_totals.index:
        return 0
    else:
        if score_totals.index.get_loc(answer[1]) > 30:
            score=0
        else:
            score=len(score_totals) - score_totals.index.get_loc(answer[1])
        return score

def most_penalty_goal(answer):
    penalty_goal_counts = df2[df2['penalty'] == True].groupby('team')['penalty'].count().sort_values(ascending=False)
    if answer[1] not in penalty_goal_counts:
        return 0
    else:
        if penalty_goal_counts.index.get_loc(answer[1]) > 10:
            score=0
        else:
            score = len(penalty_goal_counts) - penalty_goal_counts.index.get_loc(answer[1])
        return score

national_functions = [most_goal, home_goal, away_goal, most_own_goal, most_wc_goal, most_penalty_goal]