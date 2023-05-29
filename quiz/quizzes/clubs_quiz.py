import pandas as pd
from .calculator import calculate_score
df = pd.read_csv("quiz/data/clubs/football_results.csv", encoding="ISO-8859-1", usecols=['Date','Competition','Team', 'Team_Score', 'Opponent', 'Opponent_Score', 'Home_Penalties', 'Away_Penalties', 'Team_Points', 'Opponent_Points' ])

def home_goal(answer):
    home_team = df.groupby('Team')
    rank_table = home_team['Team_Score'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, 1800)

def away_goal(answer):
    away_team = df.groupby('Opponent')
    rank_table = away_team['Opponent_Score'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, 1800)
    
def most_goal(answer):
    home_team_scores = df.groupby('Team')['Team_Score'].sum()
    away_team_scores = df.groupby('Opponent')['Opponent_Score'].sum()
    team_scores = home_team_scores.add(away_team_scores, fill_value=0)
    rank_table = team_scores.sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, 1800)
    
def most_penalty(answer):
    home_penalty = df.groupby('Team')['Home_Penalties'].sum()
    away_penalty = df.groupby('Opponent')['Away_Penalties'].sum()
    team_penalty = home_penalty.add(away_penalty, fill_value=0)
    rank_table = team_penalty.sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, 1800)
    
def most_won(answer):
    home_won = df[df['Team_Points']== 3.0].groupby('Team')['Team_Points'].sum()
    away_won = df[df['Opponent_Points']==3.0].groupby('Opponent')['Opponent_Points'].sum()
    rank_table = home_won.add(away_won, fill_value=0)
    return calculate_score(answer[1], rank_table, 1000)
    
def most_draw(answer):
    home_draw = df[df['Team_Points'] == 1.0].groupby('Team')['Team_Points'].sum()
    away_draw = df[df['Opponent_Points'] == 1.0 ].groupby('Opponent')['Opponent_Points'].sum()
    rank_table = home_draw.add(away_draw, fill_value=0)
    return calculate_score(answer[1], rank_table, 400)
    
question = ['Most Home Goal', 'Most Away Goal', "Most Goal", "Most Penalty Scored", 'Most Won', 'Most Draw']
clubs_functions = [home_goal, away_goal, most_goal, most_penalty, most_won, most_draw]