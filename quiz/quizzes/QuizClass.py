from mongo_connection import client
class QuizClass:
    db = client["Quiz"]

    @classmethod
    def info(cls):
        raise NotImplementedError("Subclasses must implement info() method.")

    @classmethod
    def calculate_score(_, answer, rank_table, top=100):
        """
        Calculate the score based on the answers and rank table.

        Args:
            answer (dict): A dictionary containing players divided by position.
            rank_table (DataFrame): The rank table containing player rankings.
            top (int, optional): The maximum rank to consider as "best". Defaults to 100.

        Returns:
            int: The calculated score.

        """

        # Checking if answer is in the rank_table
        if answer not in rank_table:
            return 0
        else:
            # Checking if answer is in the top ranks
            if rank_table.index.get_loc(answer) > top:
                score = 0
            else:
                score = 100 - rank_table.index.get_loc(answer)
            return score

    @classmethod
    def result(cls, items):
        score = 0
        for answer, cls.function in zip(items, cls.functions):
            score += cls.function(answer)
        return score
