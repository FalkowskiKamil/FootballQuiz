import pandas as pd
from .QuizClass import QuizClass


class StadiumQuiz(QuizClass):
    collection = QuizClass.db['stadium_quiz']
    df = pd.DataFrame(list(collection.find()))
    df["total_capacity"] = df["total_capacity"].str.replace(",", "").astype(int)

    @classmethod
    def info(cls):
        stadium2 = (
            cls.df[
                (cls.df["sport_played"] == "Football")
                & (cls.df["total_capacity"] > 15000)
            ]["country"]
            .sort_values()
            .unique
        )
        question = [
            "World biggest stadium:",
            "EU biggest stadium:",
            "SA biggest stadium:",
            "EU most +15k stadium",
            "Asia most +15k stadium",
            "Africa most +15k stadium",
        ]
        return [stadium2, None, None, None, question]

    @classmethod
    def biggest_stadium(cls, answer):
        country = cls.df.groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    @classmethod
    def eu_biggest(cls, answer):
        country = cls.df[cls.df["region"] == "Europe"].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    @classmethod
    def sa_biggest(cls, answer):
        country = cls.df[cls.df["region"] == "South America"].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    @classmethod
    def eu_most(cls, answer):
        country = cls.df[
            (cls.df["region"] == "Europe") & (cls.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    @classmethod
    def as_most(cls, answer):
        country = cls.df[
            (cls.df["region"] == "Asia") & (cls.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    @classmethod
    def af_most(cls, answer):
        country = cls.df[
            (cls.df["region"] == "Africa") & (cls.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return cls.calculate_score(answer[1], rank_table, top=5)

    functions = [biggest_stadium, eu_biggest, sa_biggest, eu_most, as_most, af_most]
