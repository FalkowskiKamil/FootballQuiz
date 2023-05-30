import pandas as pd
import numpy as np
from .calculator import calculate_score

df = pd.read_csv(
    "quiz/data/wc/wc_detail.csv",
    usecols=[
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "home_penalty",
        "away_penalty",
        "Date",
        "Host",
        "Year",
        "home_red_card",
        "away_red_card",
    ],
)
df["home_red_card"] = (
    df["home_red_card"]
    .replace([np.nan, np.inf], "")
    .str.count("·")
    .fillna(0)
    .astype(int)
)
df["away_red_card"] = (
    df["away_red_card"]
    .replace([np.nan, np.inf], "")
    .str.count("·")
    .fillna(0)
    .astype(int)
)


def info():
    nations = df["home_team"].sort_values().unique
    date = df["Date"]
    questions = [
        "Most apperance",
        "Most Goals",
        "Most Penalty Scored",
        "Most conceded goal",
        "Most Red card",
        "Most Goal/Apperance",
    ]
    return [nations, date.iloc[-1], date[0], None, questions]


def apperance(answer):
    home_match = df["home_team"].value_counts()
    away_match = df["away_team"].value_counts()
    rank_table = home_match.add(away_match).sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=30)


def score_goal(answer):
    home_scores = df.groupby("home_team")["home_score"].sum()
    away_scores = df.groupby("away_team")["away_score"].sum()
    rank_table = home_scores.add(away_scores, fill_value=0).sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=30)


def penalty_goal(answer):
    home_penalty = df.groupby("home_team")["home_penalty"].sum()
    away_penalty = df.groupby("away_team")["away_penalty"].sum()
    rank_table = home_penalty.add(away_penalty, fill_value=0).sort_values(
        ascending=False
    )
    return calculate_score(answer[1], rank_table, top=30)


def conceded_goal(answer):
    home_conceded = df.groupby("home_team")["away_score"].sum()
    away_conceded = df.groupby("away_team")["home_score"].sum()
    rank_table = home_conceded.add(away_conceded, fill_value=0).sort_values(
        ascending=False
    )
    return calculate_score(answer[1], rank_table, top=30)


def most_red(answer):
    home_red = df.groupby("home_team")["home_red_card"].sum()
    away_red = df.groupby("away_team")["away_red_card"].sum()
    rank_table = home_red.add(away_red, fill_value=0).sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=30)


def goal_to_apperance(answer):
    home_goals = df.groupby("home_team")["home_score"].sum()
    away_goals = df.groupby("away_team")["away_score"].sum()
    total_goals = home_goals.add(away_goals, fill_value=0)
    matches_played = df["home_team"].value_counts() + df["away_team"].value_counts()
    rank_table = total_goals.divide(matches_played).sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=30)


wc_functions = [
    apperance,
    score_goal,
    penalty_goal,
    conceded_goal,
    most_red,
    goal_to_apperance,
]


def result(items):
    score = 0
    for answer, function in zip(items, wc_functions):
        score += function(answer)
    return score
