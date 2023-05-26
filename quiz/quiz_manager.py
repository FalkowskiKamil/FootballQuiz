from .quizzes import national_quiz, clubs_quiz, stadium_quiz,  world_cup

def get_info(type):
    if type == 'national':
        nations = national_quiz.df['home_team'].sort_values().unique
        date = national_quiz.df['date'].sort_values()
        competition =  national_quiz.df['tournament'].unique()
        question = national_quiz.question
        return [nations, date[0], date.iloc[-1], competition, question]
    
    if type == 'clubs':
        clubs = clubs_quiz.df['Team'].sort_values().unique
        date = clubs_quiz.df['Date'].sort_values()
        competition = clubs_quiz.df['Competition'].sort_values().unique
        question = clubs_quiz.question
        return [clubs, date[0], date.iloc[-1], competition, question]
    
    if type == 'stadium':
        stadium2 = stadium_quiz.df[(stadium_quiz.df['sport_played'] == 'Football') & (stadium_quiz.df['total_capacity'] > 15000)]['country'].sort_values().unique
        question= stadium_quiz.question
        return [stadium2, None, None , None, question]
    
    if type == 'wc':
        nations = world_cup.df['home_team'].sort_values().unique
        date = world_cup.df['Date']
        questions = world_cup.questions
        return [nations, date.iloc[-1], date[0],None,  questions]

def get_quiz(quiz_type, items):
    score=0
    if quiz_type=='national':
        for i, answer in enumerate(items):
            if i < len(national_quiz.national_functions):
                score += national_quiz.national_functions[i](answer)
        return score
    
    elif quiz_type=='clubs':
        for i, answer in enumerate(items):
            if i < len(clubs_quiz.clubs_functions):
                score += clubs_quiz.clubs_functions[i](answer)
        return score
    
    elif quiz_type=='stadium':
        for i, answer in enumerate(items):
            if i < len(stadium_quiz.stadium_functions):
                score += stadium_quiz.stadium_functions[i](answer)
        return score
    
    elif quiz_type=='wc':
        for i, answer in enumerate(items):
            if i <len(world_cup.functions):
                score += world_cup.functions[i](answer)
        return score