from quiz.quizzes.wc_quiz import WorldCupQuiz
from quiz.quizzes.stadium_quiz import StadiumQuiz
from quiz.quizzes.national_quiz import NationalQuiz
from quiz.quizzes.clubs_quiz import FootballQuiz


def get_info(quiz_type):
    match quiz_type:
        case "wc":
            worldcup_quiz = WorldCupQuiz()
            return worldcup_quiz.info()

        case "stadium":
            stadium = StadiumQuiz()
            return stadium.info()

        case "national":
            national = NationalQuiz()
            return national.info()

        case "clubs":
            footballquiz = FootballQuiz()
            return footballquiz.info()


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
