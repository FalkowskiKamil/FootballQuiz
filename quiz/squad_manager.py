import pandas as pd
def info():
    df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position', 'highest_market_value_in_eur'])
    df=df.sort_values(by='highest_market_value_in_eur', ascending=False)
    return df


def value_squad(answer):
    score=0
    df= info()
    for position, players in answer.items():
        position_df=df[df['position'] == str(position)]
        for player in players:
            if player in  position_df['name'].values[:30]:
                score += 100 - position_df[position_df['name'] == player].index.item()
    return score

def goal_squad(answer):
    return 5

def assist_squad(answer):
    return 5

def yellow_squad(answer):
    return 5

def get_quiz(quiz_type, items):
    items = devide_position(items)
    if quiz_type == 'value squad':
        return value_squad(items)
    elif quiz_type == 'goal squad':
        return goal_squad(items)
    elif quiz_type == 'assist squad':
        return assist_squad(items)
    elif quiz_type == 'yellow squad':
        return yellow_squad(items)
    
def devide_position(players):
    players_dict=dict()
    players_dict['Attack'] = players.getlist('striker[]')
    players_dict['Midfield'] = players.getlist('middlefielder[]')
    players_dict['Defender'] = players.getlist('defender[]')
    players_dict['Goalkeeper'] = players.get('goalkeeper')
    return players_dict