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
            score = len(home_scores) - home_scores.index.get_loc(answer[1]) - 1800
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
            score = len(away_scores) - away_scores.index.get_loc(answer[1]) - 1800
        return score
    
def most_goal(answer):
    home_team_scores = df.groupby('Team')['Team_Score'].sum()
    away_team_scores = df.groupby('Opponent')['Opponent_Score'].sum()
    team_scores = home_team_scores.add(away_team_scores, fill_value=0)
    # Rank the teams based on their scores
    ranked_teams = team_scores.sort_values(ascending=False)

    # Find the position of the given team
    if answer[1] not in ranked_teams:
        return 0
    else:
        if ranked_teams.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score = len(ranked_teams) - ranked_teams.index.get_loc(answer[1]) - 1800
        return score
    
def most_penalty(answer):
    home_penalty = df.groupby('Team')['Home_Penalties'].sum()
    away_penalty = df.groupby('Opponent')['Away_Penalties'].sum()
    team_penalty = home_penalty.add(away_penalty, fill_value=0)
    ranked_penalty = team_penalty.sort_values(ascending=False)
    if answer[1] not in ranked_penalty:
        return 0
    else:
        if ranked_penalty.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score = len(ranked_penalty) - ranked_penalty.index.get_loc(answer[1]) - 1800
        return score
    
def most_won(answer):
    home_won = df[df['Team_Points']== 3.0].groupby('Team')['Team_Points'].sum()
    away_won = df[df['Opponent_Points']==3.0].groupby('Opponent')['Opponent_Points'].sum()
    ranked_won = home_won.add(away_won, fill_value=0)
    if answer[1] not in ranked_won:
        return 0
    else:
        if ranked_won.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score = len(ranked_won) - ranked_won.index.get_loc(answer[1]) - 1000
        return score
    
def most_draw(answer):
    home_draw = df[df['Team_Points'] == 1.0].groupby('Team')['Team_Points'].sum()
    away_draw = df[df['Opponent_Points'] == 1.0 ].groupby('Opponent')['Opponent_Points'].sum()
    ranked_draw = home_draw.add(away_draw, fill_value=0)
    if answer[1] not in ranked_draw:
        return 0
    else:
        if ranked_draw.index.get_loc(answer[1]) > 100:
            score=0
        else:
            score=len(ranked_draw) - ranked_draw.index.get_loc(answer[1]) - 400
        return score


question = ['Most Home Goal', 'Most Away Goal', "Most Goal", "Most Penalty Scored", 'Most Won', 'Most Draw']
clubs_functions = [home_goal, away_goal, most_goal, most_penalty, most_won, most_draw]