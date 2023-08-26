from django.test import TestCase
from quiz import quiz_manager

class TestQuizManager(TestCase):
    def test_get_info_national(self):
        result = quiz_manager.get_info("national")
        self.assertIsNotNone(result)

    def test_get_info_clubs(self):
        result = quiz_manager.get_info("clubs")
        self.assertIsNotNone(result)

    def test_get_info_stadium(self):
        result = quiz_manager.get_info("stadium")
        self.assertIsNotNone(result)

    def test_get_info_wc(self):
        result = quiz_manager.get_info("wc")
        self.assertIsNotNone(result)

    
    def test_get_quiz_result_national(self):
        items = {"question1": "answer1", "question2": "answer2"}
        result = quiz_manager.get_quiz_result("national", items)
        self.assertIsNotNone(result)

    def test_get_quiz_result_clubs(self):
        items = {"question1": "answer1", "question2": "answer2"}
        result = quiz_manager.get_quiz_result("clubs", items)
        pytho

    def test_get_quiz_result_stadium(self):
        items = {"question1": "answer1", "question2": "answer2"}
        result = quiz_manager.get_quiz_result("stadium", items)
        self.assertIsNotNone(result)

    def test_get_quiz_result_wc(self):
        items = {"question1": "answer1", "question2": "answer2"}
        result = quiz_manager.get_quiz_result("wc", items)
        self.assertIsNotNone(result)