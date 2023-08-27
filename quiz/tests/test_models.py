from django.test import TestCase
from ..models import Quiz
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.quiz = Quiz.objects.create(user = self.user, quiz_type = "wc", score = 100)

    def test_quiz(self):
        self.assertEquals(self.quiz.score, 100)
        self.assertEquals(self.quiz.quiz_type, "wc")
        quiz_number_before_unique_test = len(Quiz.objects.all())
        Quiz.objects.create(user = self.user, quiz_type = "wc", score = 100)
        self.assertEquals(self.quiz.user, self.user)
        quiz_number_after_unique_test = len(Quiz.objects.all())
        self.assertEquals(quiz_number_before_unique_test, quiz_number_after_unique_test)