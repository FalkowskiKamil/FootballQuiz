from .quizzes.wc_quiz import WorldCupQuiz
from .quizzes.stadium_quiz import StadiumQuiz
from .quizzes.national_quiz import NationalQuiz
from .quizzes.clubs_quiz import FootballQuiz


def get_info(type):
    match type:
        case "wc":
            return WorldCupQuiz.info()

        case "stadium":
            return StadiumQuiz.info()

        case "national":
            return NationalQuiz.info()

        case "clubs":
            return FootballQuiz.info()


def get_quiz_result(quiz_type, items):
    match quiz_type:
        case "wc":
            return WorldCupQuiz.result(items)

        case "stadium":
            return StadiumQuiz.result(items)

        case "national":
            return NationalQuiz.result(items)

        case "clubs":
            return FootballQuiz.result(items)
