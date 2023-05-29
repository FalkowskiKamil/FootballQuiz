from .quizzes import national_quiz, clubs_quiz, stadium_quiz,  wc_quiz

def get_info(type):
    if type == 'national':
        return national_quiz.info()
    
    elif type == 'clubs':
        return clubs_quiz.info()
    
    elif type == 'stadium':
        return stadium_quiz.info()

    elif type == 'wc':
        return wc_quiz.info()

def get_quiz_result(quiz_type, items):
    if quiz_type=='national':
        return national_quiz.result(items)
    
    elif quiz_type=='clubs':
       return clubs_quiz.result(items)
    
    elif quiz_type=='stadium':
        return stadium_quiz.result(items)
    
    elif quiz_type=='wc':
        return wc_quiz.result(items)