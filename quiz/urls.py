from django.urls import path
from quiz import views

app_name = "football_quiz"

urlpatterns = [
    path("", views.main, name="main"),
    path("quiz/", views.main_quiz, name="main_quiz"),
    path("squad/", views.main_squad, name="main_squad"),
    path("quiz/<str:quiz_type>/", views.quiz, name="quiz"),
    path(
        "squad_challange/<str:quiz_type>/", views.squad_challange, name="squad_challange"
    ),
    path("<str:quiz_type>/result/", views.result, name="result"),
    path("ranking/<str:quiz_type>/", views.ranking, name="ranking"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
]
