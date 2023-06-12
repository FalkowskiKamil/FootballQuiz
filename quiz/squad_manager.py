import pandas as pd


def info(type):
    """
    Retrieves information from the CSV files based on the quiz type.

    Args:
        quiz_type (str): The type of quiz.

    Returns:
        pd.DataFrame: The DataFrame containing the relevant information.

    """
    match type:
        case "value squad":
            df = pd.read_csv(
                "quiz/data/squad/players.csv",
                usecols=["name", "position", "highest_market_value_in_eur"],
            )
            df = df.sort_values(by="highest_market_value_in_eur", ascending=False)

        case "goal squad":
            df = pd.read_csv(
                "quiz/data/squad/merged_appearances.csv",
                usecols=["name", "goals", "position"],
            )
            df = df.sort_values(by="goals", ascending=False)

        case "assist squad":
            df = pd.read_csv(
                "quiz/data/squad/merged_appearances.csv",
                usecols=["name", "assists", "position"],
            )
            df = df.sort_values(by="assists", ascending=False)

        case "yellow squad":
            df = pd.read_csv(
                "quiz/data/squad/merged_appearances.csv",
                usecols=["name", "yellow_cards", "position"],
            )
            df = df.sort_values(by="yellow_cards", ascending=False)
    return df


def get_squad_result(quiz_type, items):
    """
    Calculate the score for the squad quiz.

    Args:
        quiz_type (str): The type of quiz.
        items (MultiValueDict): The answers submitted by the user.

    Returns:
        int: The calculated score.

    """
    return calculate_score(devide_position(items), info(quiz_type))

def devide_position(players):
    """
    Divide the posted list of players for each position.

    Args:
        players (MultiValueDict): The submitted players.

    Returns:
        dict: A dictionary containing players divided by position.

    """
    players_dict = {
        "Attack": players.getlist("striker[]"),
        "Midfield": players.getlist("middlefielder[]"),
        "Defender": players.getlist("defender[]"),
        "Goalkeeper": players.getlist("goalkeeper"),
    }
    return players_dict


def calculate_score(answer, df):
    """
    Calculate the score based on the answers and DataFrame.

    Args:
        answer (dict): A dictionary containing players divided by position.
        df (DataFrame): The DataFrame containing the player information.

    Returns:
        int: The calculated score.

    """
    score = 0
    for position, players in answer.items():
        # Get data of 30 best matches
        position_df = df[df["position"] == position][:30].reset_index()
        for player in players:
            if player in position_df["name"].values:
                score += (
                    100 - position_df.index[position_df["name"] == player].values[0]
                )
    return score
