import pandas as pd
from .calculator import calculate_score

df = pd.read_csv("quiz/data/stadium/all_stadiums.csv", usecols=[1, 2, 5, 6])
df["total_capacity"] = df["total_capacity"].str.replace(",", "").astype(int)


def info():
    stadium2 = (
        df[(df["sport_played"] == "Football") & (df["total_capacity"] > 15000)][
            "country"
        ]
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


def biggest_stadium(answer):
    country = df.groupby("country")
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


def eu_biggest(answer):
    country = df[df["region"] == "Europe"].groupby("country")
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


def sa_biggest(answer):
    country = df[df["region"] == "South America"].groupby("country")
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


def eu_most(answer):
    country = df[(df["region"] == "Europe") & (df["total_capacity"] >= 15000)].groupby(
        "country"
    )
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


def as_most(answer):
    country = df[(df["region"] == "Asia") & (df["total_capacity"] >= 15000)].groupby(
        "country"
    )
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


def af_most(answer):
    country = df[(df["region"] == "Africa") & (df["total_capacity"] >= 15000)].groupby(
        "country"
    )
    rank_table = country["total_capacity"].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


stadium_functions = [biggest_stadium, eu_biggest, sa_biggest, eu_most, as_most, af_most]


def result(items):
    score = 0
    for i, answer in enumerate(items):
        if i < len(stadium_functions):
            score += stadium_functions[i](answer)
    return score
