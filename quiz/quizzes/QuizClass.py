import time
from utils.mongo_connection import checking_connection


class QuizClass:
    def __init__(self):
        client = checking_connection()
        while client == None:
            client = checking_connection()
            time.sleep(5)
        self.db = client["Quiz"]

    def info(self):
        raise NotImplementedError("Subclasses must implement info() method.")

    @classmethod
    def calculate_score(_, answer, rank_table, top=100):
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
        for answer, function in zip(items, cls.functions):
            score += function(cls(), answer)
        return score
