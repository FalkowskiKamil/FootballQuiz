from .quizzes.clubs_quiz import FootballQuiz
from .quizzes.stadium_quiz import StadiumQuiz
from .quizzes.national_quiz import NationalQuiz
from .quizzes.wc_quiz import WorldCupQuiz


def get_info(type):
    """
    Retrieves information from the CSV files based on the quiz type.

    Args:
        type (str): The type of quiz.

    Returns:
        pd.DataFrame: The DataFrame containing the relevant information.

    """
    match type:
        case "national":
            return NationalQuiz.info()

        case "clubs":
            return FootballQuiz.info()

        case "stadium":
            return StadiumQuiz.info()

        case "wc":
            return WorldCupQuiz.info()


def get_quiz_result(quiz_type, items):
    """
    Calculate the score for the quiz.

    Args:
        quiz_type (str): The type of quiz.
        items (MultiValueDict): The answers submitted by the user.

    Returns:
        int: The calculated score.

    """
    match quiz_type:
        case "national":
            return NationalQuiz.result(items)

        case "clubs":
            return FootballQuiz.result(items)

        case "stadium":
            return StadiumQuiz.result(items)

        case "wc":
            return WorldCupQuiz.result(items)
