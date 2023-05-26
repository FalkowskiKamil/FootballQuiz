import pandas as pd
def info():
    df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position', 'highest_market_value_in_eur'])
    df=df.sort_values(by='highest_market_value_in_eur', ascending=False)
    return df