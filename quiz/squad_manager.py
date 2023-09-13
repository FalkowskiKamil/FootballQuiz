import time
import pandas as pd
from utils.mongo_connection import checking_connection

class SquadManager():
    def __init__(self):
        client = checking_connection()
        while client == None:
            client = checking_connection()
            time.sleep(5)
        self.db = client["Squad"]

    @classmethod
    def info(cls, type):
        instance = cls()
        match type:
            case "value squad":
                collection = instance.db["players"]
                cls.df = pd.DataFrame(collection.find())
            case "goal squad":
                collection = instance.db["appearance_goals"]
                cls.df = pd.DataFrame(collection.find())
            case "assist squad":
                collection = instance.db["appearance_assists"]
                cls.df = pd.DataFrame(collection.find())
            case "yellow squad":
                collection = instance.db["appearance_yellow"]
                cls.df = pd.DataFrame(collection.find())
        return cls.df

    @classmethod
    def get_squad_result(self, quiz_type, items):
        return self.calculate_score(self.devide_position(items), self.info(quiz_type))

    @classmethod
    def devide_position(self, players):
        players_dict = {
            "Attack": players.getlist("striker[]"),
            "Midfield": players.getlist("middlefielder[]"),
            "Defender": players.getlist("defender[]"),
            "Goalkeeper": players.getlist("goalkeeper"),
        }
        return players_dict

    @classmethod
    def calculate_score(cls, answer, df):
        score = 0
        instance = cls()
        for position, players in answer.items():
            # Get data of 30 best matches
            position_df = instance.df[instance.df["position"] == position][:30].reset_index()
            for player in players:
                if player in position_df["name"].values:
                    score += (
                        100 - position_df.index[position_df["name"] == player].values[0]
                    )
        return score
