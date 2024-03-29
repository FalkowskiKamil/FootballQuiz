from django.shortcuts import render
from django.contrib.auth.models import User
from quiz.models import Quiz
from quiz.squad_manager import SquadManager
from quiz.quiz_manager import get_info, get_quiz_result
from utils.logger import configure_logger
logger = configure_logger()


def main(request):
    context = {}
    return render(request, template_name="quiz/menu_main.html", context=context)


def main_quiz(request):
    return render(request, template_name="quiz/menu_quiz.html")


def main_squad(request):
    return render(request, template_name="quiz/menu_squad.html")


def quiz(request, quiz_type):
    data = get_info(quiz_type)
    context = {
        "quiz_type": quiz_type,
        "teams": data[0],
        "first_date": data[1],
        "last_date": data[2],
        "competition": data[3],
        "questions": data[4],
    }
    return render(request, template_name="quiz/quiz.html", context=context)


def squad_challange(request, quiz_type):
    data = SquadManager.info(quiz_type)
    # Getting info of 300 best matches for each position and shuffling
    context = {
        "attack": data.loc[data["position"] == "Attack", "name"]
        .iloc[:300]
        .sample(frac=1),
        "middlefielder": data.loc[data["position"] == "Midfield", "name"]
        .iloc[:300]
        .sample(frac=1),
        "defender": data.loc[data["position"] == "Defender", "name"]
        .iloc[:300]
        .sample(frac=1),
        "goalkeeper": data.loc[data["position"] == "Goalkeeper", "name"]
        .iloc[:300]
        .sample(frac=1),
        "quiz_type": quiz_type,
    }
    return render(request, template_name="quiz/squad.html", context=context)


def result(request, quiz_type):
    context = {"score": 0}
    if request.method == "POST":
        # Checking type of posted quiz
        if "goalkeeper" in request.POST.keys():
            score = SquadManager.get_squad_result(quiz_type, request.POST)
        else:
            score = get_quiz_result(quiz_type, items=request.POST.items())
        # Saving result
        user = request.user if request.user.is_authenticated else None
        result_object = Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
        logger.debug(f"{result_object}")
        context = {"score": result_object}
    return render(request, template_name="quiz/result.html", context=context)


def ranking(request, quiz_type):
    # Checking if user ask for specific rank
    if quiz_type == "all":
        context = {
            "quiz_type": "All",
            "result": Quiz.objects.all().order_by("score").reverse,
        }
    else:
        context = {
            "quiz_type": quiz_type,
            "result": Quiz.objects.filter(quiz_type=quiz_type)
            .order_by("score")
            .reverse,
        }
    return render(request, template_name="quiz/ranking.html", context=context)


def profile(request, user_id):
    context = {
        "profile": User.objects.get(id=user_id),
        "result": Quiz.objects.filter(user=user_id)
        .order_by("quiz_type", "score")
        .reverse,
    }
    return render(request, template_name="quiz/profile.html", context=context)
