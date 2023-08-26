import pandas as pd
from utils.mongo_connection import client

db = client["Squad"]


def info(type):
    match type:
        case "value squad":
            collection = db["players"]
            df = pd.DataFrame(collection.find())
        case "goal squad":
            collection = db["appearance_goals"]
            df = pd.DataFrame(collection.find())
        case "assist squad":
            collection = db["appearance_assists"]
            df = pd.DataFrame(collection.find())
        case "yellow squad":
            collection = db["appearance_yellow"]
            df = pd.DataFrame(collection.find())
    return df


def get_squad_result(quiz_type, items):
    return calculate_score(devide_position(items), info(quiz_type))


def devide_position(players):
    players_dict = {
        "Attack": players.getlist("striker[]"),
        "Midfield": players.getlist("middlefielder[]"),
        "Defender": players.getlist("defender[]"),
        "Goalkeeper": players.getlist("goalkeeper"),
    }
    return players_dict


def calculate_score(answer, df):
    score = 0
    for position, players in answer.items():
        # Get data of 30 best matches
        position_df = df[df["position"] == position][:30].reset_index()
        for player in players:
            if player in position_df["name"].values:
                score += (
                    100 - position_df.index[position_df["name"] == player].values[0]
                )
    return score
