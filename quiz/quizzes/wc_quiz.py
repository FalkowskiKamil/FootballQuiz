import pandas as pd
from .QuizClass import QuizClass


class WorldCupQuiz(QuizClass):
    def __init__(self):
        super().__init__()
        collection = self.db["wc_quiz"]
        self.df = pd.DataFrame(list(collection.find()))

    def info(self):
        nations = self.df["home_team"].sort_values().unique
        date = self.df["Date"]
        questions = [
            "Most apperance",
            "Most Goals",
            "Most Penalty Scored",
            "Most conceded goal",
            "Most Red card",
            "Most Goal/Apperance",
        ]
        return [nations, date.iloc[-1], date[0], None, questions]

    def apperance(self, answer):
        home_match = self.df["home_team"].value_counts()
        away_match = self.df["away_team"].value_counts()
        rank_table = home_match.add(away_match).sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=30)

    def score_goal(self, answer):
        home_scores = self.df.groupby("home_team")["home_score"].sum()
        away_scores = self.df.groupby("away_team")["away_score"].sum()
        rank_table = home_scores.add(away_scores, fill_value=0).sort_values(
            ascending=False
        )
        return self.calculate_score(answer[1], rank_table, top=30)

    def penalty_goal(self, answer):
        home_penalty = self.df.groupby("home_team")["home_penalty"].sum()
        away_penalty = self.df.groupby("away_team")["away_penalty"].sum()
        rank_table = home_penalty.add(away_penalty, fill_value=0).sort_values(
            ascending=False
        )
        return self.calculate_score(answer[1], rank_table, top=30)

    def conceded_goal(self, answer):
        home_conceded = self.df.groupby("home_team")["away_score"].sum()
        away_conceded = self.df.groupby("away_team")["home_score"].sum()
        rank_table = home_conceded.add(away_conceded, fill_value=0).sort_values(
            ascending=False
        )
        return self.calculate_score(answer[1], rank_table, top=30)

    def most_red(self, answer):
        home_red = self.df.groupby("home_team")["home_red_card"].sum()
        away_red = self.df.groupby("away_team")["away_red_card"].sum()
        rank_table = home_red.add(away_red, fill_value=0).sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=30)

    def goal_to_apperance(self, answer):
        home_goals = self.df.groupby("home_team")["home_score"].sum()
        away_goals = self.df.groupby("away_team")["away_score"].sum()
        total_goals = home_goals.add(away_goals, fill_value=0)
        matches_played = (
            self.df["home_team"].value_counts() + self.df["away_team"].value_counts()
        )
        rank_table = total_goals.divide(matches_played).sort_values(ascending=False)
        return self.calculate_score(answer[1], rank_table, top=30)

    functions = [
        apperance,
        score_goal,
        penalty_goal,
        conceded_goal,
        most_red,
        goal_to_apperance,
    ]
