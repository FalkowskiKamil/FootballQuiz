from threading import Thread
import time
from utils.mongo_connection import checking_connection


class QuizClass:
    client = checking_connection
    if client == None:
        time.sleep(5)
        client = checking_connection()
    db = client()["Quiz"]

    @classmethod
    def info(cls):
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
        for answer, cls.function in zip(items, cls.functions):
            score += cls.function(answer)
        return score
