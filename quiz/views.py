from django.shortcuts import render
from . import quiz_manager, squad_manager, models
from django.contrib.auth.models import User
from manage import configure_logger
logger=configure_logger()

# Create your views here.


def main(request):
    context = {}
    context_message = request.GET.get("context")
    if context_message:
        context["message"] = context_message
    return render(request, template_name="quiz/main.html", context=context)


def main_quiz(request):
    return render(request, template_name="quiz/main_quiz.html")


def main_squad(request):
    return render(request, template_name="quiz/main_squad.html")


def result(request, quiz_type):
    if request.method == "POST":
        # Checking type of posted quiz
        if "goalkeeper" in request.POST.keys():
            score = squad_manager.get_squad_result(quiz_type, request.POST)
        else:
            score = quiz_manager.get_quiz_result(quiz_type, request.POST.items())
    # Saving result
    user = request.user if request.user.is_authenticated else None
    result = models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    logger.debug(f'{result}')
    context = {"score": result}
    return render(request, template_name="quiz/result.html", context=context)


def profile(request, user_id):
    context = {
        "profile": User.objects.get(id=user_id),
        "result": models.Quiz.objects.filter(user=user_id)
        .order_by("quiz_type", "score")
        .reverse,
    }
    return render(request, template_name="quiz/profile.html", context=context)


def ranking(request, quiz_type):
    # Checking if user ask for specific rank
    if quiz_type == "all":
        context = {
            "quiz_type": "All",
            "result": models.Quiz.objects.all().order_by("score").reverse,
        }
    else:
        context = {
            "quiz_type": quiz_type,
            "result": models.Quiz.objects.filter(quiz_type=quiz_type)
            .order_by("score")
            .reverse,
        }
    return render(request, template_name="quiz/ranking.html", context=context)


def quiz(request, quiz_type):
    data = quiz_manager.get_info(quiz_type)
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
    data = squad_manager.info(quiz_type)
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
