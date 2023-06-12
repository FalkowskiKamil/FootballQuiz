def calculate_score(answer, rank_table, top=100):
    """
    Calculate the score based on the answers and rank table.

    Args:
        answer (dict): A dictionary containing players divided by position.
        rank_table (DataFrame): The rank table containing player rankings.
        top (int, optional): The maximum rank to consider as "best". Defaults to 100.

    Returns:
        int: The calculated score.

    """

    # Checking if answer are in database
    if answer not in rank_table:
        return 0
    else:
        # Checking if answer are in best
        if rank_table.index.get_loc(answer) > top:
            score = 0
        else:
            score = 100 - rank_table.index.get_loc(answer)
        return score
