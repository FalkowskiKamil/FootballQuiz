import pandas as pd
from .QuizClass import QuizClass

class FootballQuiz(QuizClass):
    collection = QuizClass.db['clubs_quiz']
    df = pd.DataFrame(list(collection.find()))
    
    @classmethod
    def info(cls):
        clubs = cls.df["Team"].sort_values().unique()
        date = cls.df["Date"].sort_values().unique()
        competition = cls.df["Competition"].sort_values().unique()
        question = [
            "Most Home Goal",
            "Most Away Goal",
            "Most Goal",
            "Most Penalty Scored",
            "Most Won",
            "Most Draw",
        ]
        return [clubs, date[0], date[-1], competition, question]

    @classmethod
    def home_goal(cls, answer):
        home_team = cls.df.groupby("Team")
        rank_table = home_team["Team_Score"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def away_goal(cls, answer):
        away_team = cls.df.groupby("Opponent")
        rank_table = away_team["Opponent_Score"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_goal(cls, answer):
        home_team_scores = cls.df.groupby("Team")["Team_Score"].sum()
        away_team_scores = cls.df.groupby("Opponent")["Opponent_Score"].sum()
        team_scores = home_team_scores.add(away_team_scores, fill_value=0)
        rank_table = team_scores.sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_penalty(cls, answer):
        home_penalty = cls.df.groupby("Team")["Home_Penalties"].sum()
        away_penalty = cls.df.groupby("Opponent")["Away_Penalties"].sum()
        team_penalty = home_penalty.add(away_penalty, fill_value=0)
        rank_table = team_penalty.sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_won(cls, answer):
        home_won = (
            cls.df[cls.df["Team_Points"] == 3.0].groupby("Team")["Team_Points"].sum()
        )
        away_won = (
            cls.df[cls.df["Opponent_Points"] == 3.0]
            .groupby("Opponent")["Opponent_Points"]
            .sum()
        )
        rank_table = home_won.add(away_won, fill_value=0)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_draw(cls, answer):
        home_draw = (
            cls.df[cls.df["Team_Points"] == 1.0].groupby("Team")["Team_Points"].sum()
        )
        away_draw = (
            cls.df[cls.df["Opponent_Points"] == 1.0]
            .groupby("Opponent")["Opponent_Points"]
            .sum()
        )
        rank_table = home_draw.add(away_draw, fill_value=0)
        return cls.calculate_score(answer[1], rank_table)


    functions = [home_goal, away_goal, most_goal, most_penalty, most_won, most_draw]
