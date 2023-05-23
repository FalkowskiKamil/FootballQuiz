from .quizzes import national_quiz
from .quizzes import clubs_quiz

def get_info(type):
    if type == 'nation':
        nations = national_quiz.df['home_team'].sort_values().unique
        date = national_quiz.df['date'].sort_values()
        return [nations, date[0], date.iloc[-1]]
    
    if type == 'clubs':
        clubs = clubs_quiz.df['Team'].sort_values().unique
        date = clubs_quiz.df['Date'].sort_values()
        competition = clubs_quiz.df['Competition'].sort_values().unique
        return [clubs, date[0], date.iloc[-1], competition]
    
def national(items):
    score=0
    for i, answer in enumerate(items):
        if i < len(national_quiz.national_functions):
            score += national_quiz.national_functions[i](answer)
    return score
        
def clubs(items):
    score=0
    #for i, answer in enumerate(items):
        #if i < len(clubs_quiz.clubs_functions):
            #score += clubs_quiz.clubs_function[i](answer)
    return score