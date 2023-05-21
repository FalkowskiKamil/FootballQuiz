from .quizzes import national_quiz

def get_info(type):
    if type == 'nation':
        return national_quiz.df['home_team'].sort_values().unique
    
def national(items):
    score=0
    for i, answer in enumerate(items):
        if i < len(national_quiz.national_functions):
            score += national_quiz.national_functions[i](answer)
    return score
        