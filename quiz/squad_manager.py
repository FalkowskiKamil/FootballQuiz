import pandas as pd
def info(type):
    if type == 'value squad':
        df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position', 'highest_market_value_in_eur'])
        df=df.sort_values(by='highest_market_value_in_eur', ascending=False)
    elif type == 'goal squad':
        df = pd.read_csv("quiz/data/squad/merged_appearances.csv", usecols=['name', 'goals', 'position'])
        df =  df.sort_values(by='goals', ascending=False)
    elif type == 'assist squad':
        return
    elif type == 'yellow squad':
        return 
    return df


def value_squad(answer):
    score=0
    df= info('value squad')
    for position, players in answer.items():
        position_df=df[df['position'] == position][:30].reset_index()
        for player in players:
            if player in  position_df['name'].values:
                score+= 100- position_df.index[position_df['name'] == player].values[0]
    return score

def goal_squad(answer):
    score = 0
    df = info('goal squad')
    for position, players in answer.items():
        position_df=df[df['position'] == position][:30].reset_index()
        for player in players:
            if player in position_df['name'].values:
                score +=100-position_df.index[position_df['name'] == player].values[0]
    return score

def assist_squad(answer):
    return 5

def yellow_squad(answer):
    return 5

def get_squad_result(quiz_type, items):
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
    players_dict={
        'Attack': players.getlist('striker[]'),
        'Midfield': players.getlist('middlefielder[]'),
        'Defender': players.getlist('defender[]'),
        'Goalkeeper': players.getlist('goalkeeper')}
    return players_dict