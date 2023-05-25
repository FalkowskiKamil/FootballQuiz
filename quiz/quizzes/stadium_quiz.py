import pandas as pd
df = pd.read_csv("quiz/data/stadium/all_stadiums.csv", usecols=[1,2,5,6])
df['total_capacity'] = df['total_capacity'].str.replace(',', '').astype(int)

def biggest_stadium(answer):
    country = df.groupby('country')
    biggest_stadium = country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in biggest_stadium:
        return 0
    else:
        if biggest_stadium.index.get_loc(answer[1]) >30:
            score=0
        else:
            score = len(biggest_stadium) - biggest_stadium.index.get_loc(answer[1])
        return score

def eu_biggest(answer):
    country = df[df['region']=='Europe'].groupby('country')
    biggest_stadium = country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in biggest_stadium:
        return 0
    else:
        if biggest_stadium.index.get_loc(answer[1]) >5:
            score=0
        else:
            score = len(biggest_stadium) - biggest_stadium.index.get_loc(answer[1])
        return score

def sa_biggest(answer):
    country = df[df['region']=='South America'].groupby('country')
    biggest_stadium = country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in biggest_stadium:
        return 0
    else:
        if biggest_stadium.index.get_loc(answer[1]) >3:
            score=0
        else:
            score=0
            #score = len(biggest_stadium) - biggest_stadium.index.get_loc(answer[1])
        return score

def eu_most(answer):
    country = df[(df['region']=='Europe') & (df['total_capacity'] >= 15000)].groupby('country')
    most_stadium=country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in most_stadium:
        return 0
    else:
        if most_stadium.index.get_loc(answer[1]) >5 :
            score=0
        else:
            score = len(most_stadium) - most_stadium.index.get_loc(answer[1])
        return score

def as_most(answer):
    country = df[(df['region']=='Asia') & (df['total_capacity'] >= 15000)].groupby('country')
    most_stadium=country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in most_stadium:
        return 0
    else:
        if most_stadium.index.get_loc(answer[1]) >5 :
            score=0
        else:
            score = len(most_stadium) - most_stadium.index.get_loc(answer[1])
        return score
    
def af_most(answer):
    country = df[(df['region']=='Africa') & (df['total_capacity'] >= 15000)].groupby('country')
    most_stadium=country['total_capacity'].count().sort_values(ascending=False)
    if answer[1] not in most_stadium:
        return 0
    else:
        if most_stadium.index.get_loc(answer[1]) >5 :
            score=0
        else:
            score = len(most_stadium) - most_stadium.index.get_loc(answer[1])
        return score


question=['World biggest stadium:', 'EU biggest stadium:', 'SA biggest stadium:', 'EU most +15k stadium', 'Asia most +15k stadium', 'Africa most +15k stadium']
stadium_functions = [biggest_stadium,eu_biggest,sa_biggest,eu_most,as_most,af_most]