import pandas as pd
from .QuizClass import QuizClass


class StadiumQuiz(QuizClass):
    def __init__(self):
        super().__init__()
        collection = self.db["stadium_quiz"]
        self.df = pd.DataFrame(list(collection.find()))
    
    def info(self):
        stadium = self.df["country"].sort_values().unique
        question = [
            "World biggest stadium:",
            "EU biggest stadium:",
            "SA biggest stadium:",
            "EU most +15k stadium",
            "Asia most +15k stadium",
            "Africa most +15k stadium",
        ]
        return [stadium, None, None, None, question]
    
    def biggest_stadium(self, answer):
        country = self.df.groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)
    
    def eu_biggest(self, answer):
        country = self.df[self.df["region"] == "Europe"].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)
    
    def sa_biggest(self, answer):
        country = self.df[self.df["region"] == "South America"].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)
    
    def eu_most(self, answer):
        country = self.df[
            (self.df["region"] == "Europe") & (self.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)
    
    def as_most(self, answer):
        country = self.df[
            (self.df["region"] == "Asia") & (self.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)
    
    def af_most(self, answer):
        country = self.df[
            (self.df["region"] == "Africa") & (self.df["total_capacity"] >= 15000)
        ].groupby("country")
        rank_table = country["total_capacity"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=5)

    functions = [biggest_stadium, eu_biggest, sa_biggest, eu_most, as_most, af_most]
