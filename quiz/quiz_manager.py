from .quizzes import national_quiz, clubs_quiz, stadium_quiz, wc_quiz


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
            return national_quiz.info()

        case "clubs":
            return clubs_quiz.info()

        case "stadium":
            return stadium_quiz.info()

        case "wc":
            return wc_quiz.info()


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
            return national_quiz.result(items)

        case "clubs":
            return clubs_quiz.result(items)

        case "stadium":
            return stadium_quiz.result(items)

        case "wc":
            return wc_quiz.result(items)
