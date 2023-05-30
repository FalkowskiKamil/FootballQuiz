from .quizzes import national_quiz, clubs_quiz, stadium_quiz, wc_quiz


def get_info(type):
    match type:
        case "national":
            return national_quiz.info()

        case "clubs":
            return clubs_quiz.info()

        case "stadium":
            return stadium_quiz.info()

        case "wc":
            return wc_quiz.info()


def get_quiz_result(quiz_type, items):
    match quiz_type:
        case "national":
            return national_quiz.result(items)

        case "clubs":
            return clubs_quiz.result(items)

        case "stadium":
            return stadium_quiz.result(items)

        case "wc":
            return wc_quiz.result(items)
