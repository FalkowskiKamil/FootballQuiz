import pandas as pd
from .QuizClass import QuizClass


class NationalQuiz(QuizClass):
    def __init__(self):
        super().__init__()
        collection_1 = self.db["national_quiz_results"]
        self.df = pd.DataFrame(list(collection_1.find()))

        collection_2 = self.db["national_quiz_goalscorers"]
        self.df2 = pd.DataFrame(list(collection_2.find()))

    
    def info(self):
        nations = self.df["home_team"].sort_values().unique
        date = self.df["date"].sort_values()
        competition = self.df["tournament"].unique()
        question = [
            "Most Goal",
            "Most Home Goal",
            "Most Away Goal",
            "Most Own Goal",
            "Most World Cup",
            "Most Penalty Scored",
        ]
        return [nations, date[0], date.iloc[-1], competition, question]

    
    def home_goal(self, answer):
        home_team = self.df.groupby("home_team")
        rank_table = home_team["home_score"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)

    
    def away_goal(self, answer):
        away_team = self.df.groupby("away_team")
        rank_table = away_team["away_score"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)

    
    def most_goal(self, answer):
        most_goal = self.df2.groupby("team")
        rank_table = most_goal["team"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)

    
    def most_own_goal(self, answer):
        rank_table = (
            self.df2[self.df2["own_goal"] == True]
            .groupby("team")["own_goal"]
            .count()
            .sort_values(ascending=False)
        )
        return self.calculate_score(answer[1], rank_table)

    
    def most_wc_goal(self, answer):
        world_cup_data = self.df[self.df["tournament"] == "FIFA World Cup"]
        score_totals = world_cup_data.groupby(["country"])[
            "home_score", "away_score"
        ].sum()
        rank_table = score_totals["home_score"] + score_totals["away_score"]
        return self.calculate_score(answer[1], rank_table)

    
    def most_penalty_goal(self, answer):
        rank_table = (
            self.df2[self.df2["penalty"] == True]
            .groupby("team")["penalty"]
            .count()
            .sort_values(ascending=False)
        )
        return self.calculate_score(answer[1], rank_table)

    functions = [
        most_goal,
        home_goal,
        away_goal,
        most_own_goal,
        most_wc_goal,
        most_penalty_goal,
    ]
