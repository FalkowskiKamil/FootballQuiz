from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.main_url = reverse("quiz:main")
        self.main_quiz_url = reverse("quiz:main_quiz")
        self.main_squad_url = reverse("quiz:main_squad")
        self.quiz_url = reverse("quiz:quiz", args = ["wc"])
        self.squad_challage_url = reverse("quiz:squad_challange", args = ["value squad"])
        self.result_url = reverse("quiz:result", kwargs = {"quiz_type" : "wc"})
        self.ranking_url = reverse("quiz:ranking", args = ["all"])
        self.profile_url = reverse("quiz:profile", args = [1])

    def test_main_get(self):
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/menu_main.html")

    def test_main_quiz_get(self):
        response = self.client.get(self.main_quiz_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/menu_quiz.html")

    def test_main_squad_get(self):
        response = self.client.get(self.main_squad_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/menu_squad.html")

    def test_quiz_get(self):
        response = self.client.get(self.quiz_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/quiz.html")

    def test_squad_challange_get(self):
        response = self.client.get(self.squad_challage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/squad.html")

    def test_result_get(self):
        response = self.client.get(self.result_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/result.html")

    def test_ranking_get(self):
        response = self.client.get(self.ranking_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/ranking.html")

    def test_profile_get(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "quiz/profile.html")
        
    def test_result_post(self):
        response = self.client.post(self.ranking_url,
                                    {"quiz_type":"wc",
                                     "items":""
                                     }
                                    )
        self.assertEquals(response.status_code, 200)