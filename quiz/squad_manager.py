import pandas as pd
def info():
    df = pd.read_csv("quiz/data/squad/players.csv", usecols=['name','position', 'highest_market_value_in_eur'])
    df=df.sort_values(by='highest_market_value_in_eur', ascending=False)
    return df


def value_squad(answer):
    if len(answer[0])==2:#striker
        return 5
    
    return answer[0]

def goal_squad(answer):
    return 5

def assist_squad(answer):
    return 5

def yellow_squad(answer):
    return 5

def get_quiz(quiz_type, items):
    if quiz_type == 'value squad':
        return value_squad(items)
    elif quiz_type == 'goal squad':
        return goal_squad(items)
    elif quiz_type == 'assist squad':
        return assist_squad(items)
    elif quiz_type == 'yellow squad':
        return yellow_squad(items)