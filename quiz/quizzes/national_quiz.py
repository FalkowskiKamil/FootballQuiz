import pandas as pd
from .QuizClass import QuizClass


class NationalQuiz(QuizClass):
    collection_1 = QuizClass.db["national_quiz_results"]
    df = pd.DataFrame(list(collection_1.find()))

    collection_2 = QuizClass.db["national_quiz_goalscorers"]
    df2 = pd.DataFrame(list(collection_2.find()))

    @classmethod
    def info(cls):
        nations = cls.df["home_team"].sort_values().unique
        date = cls.df["date"].sort_values()
        competition = cls.df["tournament"].unique()
        question = [
            "Most Goal",
            "Most Home Goal",
            "Most Away Goal",
            "Most Own Goal",
            "Most World Cup",
            "Most Penalty Scored",
        ]
        return [nations, date[0], date.iloc[-1], competition, question]

    @classmethod
    def home_goal(cls, answer):
        home_team = cls.df.groupby("home_team")
        rank_table = home_team["home_score"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def away_goal(cls, answer):
        away_team = cls.df.groupby("away_team")
        rank_table = away_team["away_score"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_goal(cls, answer):
        most_goal = cls.df2.groupby("team")
        rank_table = most_goal["team"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_own_goal(cls, answer):
        rank_table = (
            cls.df2[cls.df2["own_goal"] == True]
            .groupby("team")["own_goal"]
            .count()
            .sort_values(ascending=False)
        )
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_wc_goal(cls, answer):
        world_cup_data = cls.df[cls.df["tournament"] == "FIFA World Cup"]
        score_totals = world_cup_data.groupby(["country"])[
            "home_score", "away_score"
        ].sum()
        rank_table = score_totals["home_score"] + score_totals["away_score"]
        return cls.calculate_score(answer[1], rank_table)

    @classmethod
    def most_penalty_goal(cls, answer):
        rank_table = (
            cls.df2[cls.df2["penalty"] == True]
            .groupby("team")["penalty"]
            .count()
            .sort_values(ascending=False)
        )
        return cls.calculate_score(answer[1], rank_table)

    functions = [
        most_goal,
        home_goal,
        away_goal,
        most_own_goal,
        most_wc_goal,
        most_penalty_goal,
    ]
