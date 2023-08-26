from django.test import SimpleTestCase
from django.urls import reverse, resolve
from quiz.views import main, main_quiz, main_squad, quiz, squad_challange, result, ranking, profile


class TestUrls(SimpleTestCase):
    def test_main_url_is_resolved(self):
        url = reverse("quiz:main")
        self.assertEquals(resolve(url).func, main)

    def test_main_quiz_url_is_resolved(self):
        url = reverse("quiz:main_quiz")
        self.assertEquals(resolve(url).func, main_quiz)

    def test_main_squad_url_is_resolved(self):
        url = reverse("quiz:main_squad")
        self.assertEquals(resolve(url).func, main_squad)

    def test_quiz_url_is_resolved(self):
        url = reverse("quiz:quiz", args = ['wc'])
        self.assertEquals(resolve(url).func, quiz)

    def test_squad_challange_url_is_resolved(self):
        url = reverse("quiz:squad_challange", args = ['value squad'])
        self.assertEquals(resolve(url).func, squad_challange)

    def test_result_url_is_resolved(self):
        url = reverse("quiz:result", args = ['wc'])
        self.assertEquals(resolve(url).func, result)

    def test_ranking_url_is_resolved(self):
        url = reverse("quiz:ranking", args = ["all"])
        self.assertEquals(resolve(url).func, ranking)

    def test_profile_url_is_resolved(self):
        url = reverse("quiz:profile", args = [1])
        self.assertEquals(resolve(url).func, profile)
