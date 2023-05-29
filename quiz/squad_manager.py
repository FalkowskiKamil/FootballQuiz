import pandas as pd
def info(type):
    if type == 'value squad':
        df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position', 'highest_market_value_in_eur'])
        df=df.sort_values(by='highest_market_value_in_eur', ascending=False)
    
    elif type == 'goal squad':
        df = pd.read_csv("quiz/data/squad/merged_appearances.csv", usecols=['name', 'goals', 'position'])
        df =  df.sort_values(by='goals', ascending=False)
    
    elif type == 'assist squad':
        df = pd.read_csv("quiz/data/squad/merged_appearances.csv", usecols=['name', 'assists', 'position'])
        df =  df.sort_values(by='assists', ascending=False)
    
    elif type == 'yellow squad':
        df = pd.read_csv("quiz/data/squad/merged_appearances.csv", usecols=['name', 'yellow_cards', 'position'])
        df =  df.sort_values(by='yellow_cards', ascending=False)
    
    return df

def get_squad_result(quiz_type, items):
    return calculate_score(devide_position(items), info(quiz_type))
    
def devide_position(players):
    #Divide posted list for each position
    players_dict={
        'Attack': players.getlist('striker[]'),
        'Midfield': players.getlist('middlefielder[]'),
        'Defender': players.getlist('defender[]'),
        'Goalkeeper': players.getlist('goalkeeper')}
    return players_dict

def calculate_score(answer, df):
    score=0
    for position, players in answer.items():
        #Get data of 30 best matches
        position_df=df[df['position'] == position][:30].reset_index()
        for player in players:
            if player in position_df['name'].values:
                score +=100-position_df.index[position_df['name'] == player].values[0]
    return score