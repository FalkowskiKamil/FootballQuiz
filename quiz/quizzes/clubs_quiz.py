import pandas as pd
from .QuizClass import QuizClass


class FootballQuiz(QuizClass):
    def __init__(self):
        super().__init__()
        collection = self.db["clubs_quiz"]
        self.df = pd.DataFrame(list(collection.find()))
    
    def info(self):
        clubs = self.df["Team"].sort_values().unique()
        date = self.df["Date"].sort_values().unique()
        competition = self.df["Competition"].sort_values().unique()
        question = [
            "Most Home Goal",
            "Most Away Goal",
            "Most Goal",
            "Most Penalty Scored",
            "Most Won",
            "Most Draw",
        ]
        return [clubs, date[0], date[-1], competition, question]
    
    def home_goal(self, answer):
        home_team = self.df.groupby("Team")
        rank_table = home_team["Team_Score"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)
    
    def away_goal(self, answer):
        away_team = self.df.groupby("Opponent")
        rank_table = away_team["Opponent_Score"].count().sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)
    
    def most_goal(self, answer):
        home_team_scores = self.df.groupby("Team")["Team_Score"].sum()
        away_team_scores = self.df.groupby("Opponent")["Opponent_Score"].sum()
        team_scores = home_team_scores.add(away_team_scores, fill_value=0)
        rank_table = team_scores.sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)
    
    def most_penalty(self, answer):
        home_penalty = self.df.groupby("Team")["Home_Penalties"].sum()
        away_penalty = self.df.groupby("Opponent")["Away_Penalties"].sum()
        team_penalty = home_penalty.add(away_penalty, fill_value=0)
        rank_table = team_penalty.sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table)
    
    def most_won(self, answer):
        home_won = (
            self.df[self.df["Team_Points"] == 3.0].groupby("Team")["Team_Points"].sum()
        )
        away_won = (
            self.df[self.df["Opponent_Points"] == 3.0]
            .groupby("Opponent")["Opponent_Points"]
            .sum()
        )
        rank_table = home_won.add(away_won, fill_value=0)
        return self.calculate_score(answer[1], rank_table)
    
    def most_draw(self, answer):
        home_draw = (
            self.df[self.df["Team_Points"] == 1.0].groupby("Team")["Team_Points"].sum()
        )
        away_draw = (
            self.df[self.df["Opponent_Points"] == 1.0]
            .groupby("Opponent")["Opponent_Points"]
            .sum()
        )
        rank_table = home_draw.add(away_draw, fill_value=0)
        return self.calculate_score(answer[1], rank_table)

    functions = [home_goal, away_goal, most_goal, most_penalty, most_won, most_draw]
