import pandas as pd
from .calculator import calculate_score
df = pd.read_csv("quiz/data/stadium/all_stadiums.csv", usecols=[1,2,5,6])
df['total_capacity'] = df['total_capacity'].str.replace(',', '').astype(int)

def biggest_stadium(answer):
    country = df.groupby('country')
    rank_table = country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)

def eu_biggest(answer):
    country = df[df['region']=='Europe'].groupby('country')
    rank_table = country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)

def sa_biggest(answer):
    country = df[df['region']=='South America'].groupby('country')
    rank_table = country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)

def eu_most(answer):
    country = df[(df['region']=='Europe') & (df['total_capacity'] >= 15000)].groupby('country')
    rank_table=country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)

def as_most(answer):
    country = df[(df['region']=='Asia') & (df['total_capacity'] >= 15000)].groupby('country')
    rank_table=country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)
    
def af_most(answer):
    country = df[(df['region']=='Africa') & (df['total_capacity'] >= 15000)].groupby('country')
    rank_table=country['total_capacity'].count().sort_values(ascending=False)
    return calculate_score(answer[1], rank_table, top=5)


question=['World biggest stadium:', 'EU biggest stadium:', 'SA biggest stadium:', 'EU most +15k stadium', 'Asia most +15k stadium', 'Africa most +15k stadium']
stadium_functions = [biggest_stadium,eu_biggest,sa_biggest,eu_most,as_most,af_most]