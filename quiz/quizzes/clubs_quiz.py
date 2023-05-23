import pandas as pd
df = pd.read_csv("quiz/data/clubs/football_results.csv", encoding="ISO-8859-1")

def home_goal(answer):
    home_team = df.groupby('Team')
    home_scores = home_team['Team_Score'].count().sort_values(ascending=False)
    if answer[1] not in home_scores:
        return 0
    else:
        if home_scores.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score = len(home_scores) - home_scores.index.get_loc(answer[1])
            score=10000
        return score

def away_goal(answer):
    away_team = df.groupby('Opponent')
    away_scores = away_team['Opponent_Score'].count().sort_values(ascending=False)
    if answer[1] not in away_scores:
        return 0
    else:
        if away_scores.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score = len(away_scores) - away_scores.index.get_loc(answer[1])
        return score

clubs_functions = [home_goal, away_goal]