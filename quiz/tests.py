from django.test import TestCase, Client
from django.urls import reverse
from . import squad_manager, quiz_manager
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Quiz
import pandas as pd

class QuizViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.main_url = reverse('quiz:main')
        self.main_quiz_url = reverse('quiz:main_quiz')
        self.main_squad_url = reverse('quiz:main_squad')
        self.quiz_url = reverse('quiz:quiz', args=['quiz_type'])
        self.result_url = reverse('quiz:result', args=['quiz_type'])
        self.profile_url = reverse('quiz:profile', args=[1])
        self.ranking_url = reverse('quiz:ranking', args=['quiz_type'])
        self.squad_challange_url = reverse('quiz:squad_challange', args=['quiz_type'])

    def test_main_view(self):
        response = self.client.get(self.main_url)
        self.assertEqual(response.status_code, 200)

    def test_main_quiz_view(self):
        response = self.client.get(self.main_quiz_url)
        self.assertEqual(response.status_code, 200)

    def test_main_squad_view(self):
        response = self.client.get(self.main_squad_url)
        self.assertEqual(response.status_code, 200)

    def test_ranking_view(self):
        response = self.client.get(self.ranking_url)
        self.assertEqual(response.status_code, 200)

class SquadManagerTestCase(TestCase):
    def test_info_value_squad(self):
        result = squad_manager.info('value squad')
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_goal_squad(self):
        result = squad_manager.info('goal squad')
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_assist_squad(self):
        result = squad_manager.info('assist squad')
        self.assertIsInstance(result, pd.DataFrame)

    def test_info_yellow_squad(self):
        result = squad_manager.info('yellow squad')
        self.assertIsInstance(result, pd.DataFrame)

class QuizManagerTestCase(TestCase):
    def test_get_info_national(self):
        result = quiz_manager.get_info('national')
        self.assertIsNotNone(result)
    
    def test_get_info_clubs(self):
        result = quiz_manager.get_info('clubs')
        self.assertIsNotNone(result)
    
    def test_get_info_stadium(self):
        result = quiz_manager.get_info('stadium')
        self.assertIsNotNone(result)
    
    def test_get_info_wc(self):
        result = quiz_manager.get_info('wc')
        self.assertIsNotNone(result)
    
    def test_get_quiz_result_national(self):
        items = {'question1': 'answer1', 'question2': 'answer2'}
        result = quiz_manager.get_quiz_result('national', items)
        self.assertIsNotNone(result)
    
    def test_get_quiz_result_clubs(self):
        items = {'question1': 'answer1', 'question2': 'answer2'}
        result = quiz_manager.get_quiz_result('clubs', items)
        self.assertIsNotNone(result)
    
    def test_get_quiz_result_stadium(self):
        items = {'question1': 'answer1', 'question2': 'answer2'}
        result = quiz_manager.get_quiz_result('stadium', items)
        self.assertIsNotNone(result)
    
    def test_get_quiz_result_wc(self):
        items = {'question1': 'answer1', 'question2': 'answer2'}
        result = quiz_manager.get_quiz_result('wc', items)
        self.assertIsNotNone(result)

class QuizModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_quiz_creation(self):
        quiz = Quiz.objects.create(
            user=self.user,
            quiz_type='national',
            score=80
        )
        self.assertIsInstance(quiz, Quiz)
        self.assertEqual(quiz.user, self.user)
        self.assertEqual(quiz.quiz_type, 'national')
        self.assertEqual(quiz.score, 80)
        self.assertIsNotNone(quiz.date)

    def test_quiz_str_representation(self):
        quiz = Quiz.objects.create(
            user=self.user,
            quiz_type='clubs',
            score=90
        )
        expected_str = f"User: {self.user} got: 90 in quiz: clubs"
        self.assertEqual(str(quiz), expected_str)

    def test_quiz_save_existing_quiz(self):
        Quiz.objects.create(
            user=self.user,
            quiz_type='stadium',
            score=70
        )

        quiz = Quiz(
            user=self.user,
            quiz_type='stadium',
            score=70
        )
        quiz.save()

        # Existing quiz found, the date should be updated
        updated_quiz = Quiz.objects.get(user=self.user, quiz_type='stadium', score=70)
        self.assertNotEqual(quiz.date, updated_quiz.date)

    def test_quiz_save_new_quiz(self):
        quiz = Quiz(
            user=self.user,
            quiz_type='wc',
            score=85
        )
        quiz.save()

        saved_quiz = Quiz.objects.get(user=self.user, quiz_type='wc', score=85)
        self.assertEqual(quiz.date, saved_quiz.date)

        # Use timezone.now() for comparison instead of naive datetime
        self.assertEqual(quiz.date, timezone.now())