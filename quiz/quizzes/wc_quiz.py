import pandas as pd
import numpy as np
from .QuizClass import QuizClass


class WorldCupQuiz(QuizClass):
    collection = QuizClass.db["wc_quiz"]
    df = pd.DataFrame(list(collection.find()))

    @classmethod
    def info(cls):
        nations = cls.df["home_team"].sort_values().unique
        date = cls.df["Date"]
        questions = [
            "Most apperance",
            "Most Goals",
            "Most Penalty Scored",
            "Most conceded goal",
            "Most Red card",
            "Most Goal/Apperance",
        ]
        return [nations, date.iloc[-1], date[0], None, questions]

    @classmethod
    def apperance(cls, answer):
        home_match = cls.df["home_team"].value_counts()
        away_match = cls.df["away_team"].value_counts()
        rank_table = home_match.add(away_match).sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=30)

    @classmethod
    def score_goal(cls, answer):
        home_scores = cls.df.groupby("home_team")["home_score"].sum()
        away_scores = cls.df.groupby("away_team")["away_score"].sum()
        rank_table = home_scores.add(away_scores, fill_value=0).sort_values(
            ascending=False
        )
        return cls.calculate_score(answer[1], rank_table, top=30)

    @classmethod
    def penalty_goal(cls, answer):
        home_penalty = cls.df.groupby("home_team")["home_penalty"].sum()
        away_penalty = cls.df.groupby("away_team")["away_penalty"].sum()
        rank_table = home_penalty.add(away_penalty, fill_value=0).sort_values(
            ascending=False
        )
        return cls.calculate_score(answer[1], rank_table, top=30)

    @classmethod
    def conceded_goal(cls, answer):
        home_conceded = cls.df.groupby("home_team")["away_score"].sum()
        away_conceded = cls.df.groupby("away_team")["home_score"].sum()
        rank_table = home_conceded.add(away_conceded, fill_value=0).sort_values(
            ascending=False
        )
        return cls.calculate_score(answer[1], rank_table, top=30)

    @classmethod
    def most_red(cls, answer):
        home_red = cls.df.groupby("home_team")["home_red_card"].sum()
        away_red = cls.df.groupby("away_team")["away_red_card"].sum()
        rank_table = home_red.add(away_red, fill_value=0).sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=30)

    @classmethod
    def goal_to_apperance(cls, answer):
        home_goals = cls.df.groupby("home_team")["home_score"].sum()
        away_goals = cls.df.groupby("away_team")["away_score"].sum()
        total_goals = home_goals.add(away_goals, fill_value=0)
        matches_played = (
            cls.df["home_team"].value_counts() + cls.df["away_team"].value_counts()
        )
        rank_table = total_goals.divide(matches_played).sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=30)

    functions = [
        apperance,
        score_goal,
        penalty_goal,
        conceded_goal,
        most_red,
        goal_to_apperance,
    ]
