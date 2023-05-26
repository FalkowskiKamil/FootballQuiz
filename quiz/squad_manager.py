import pandas as pd
def info():
    df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position'])
    return df