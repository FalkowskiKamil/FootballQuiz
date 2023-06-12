from django.shortcuts import render
from . import quiz_manager, squad_manager, models
from django.contrib.auth.models import User
from manage import configure_logger

logger = configure_logger()

# Create your views here.


def main(request):
    """
    Renders the main page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
    context = {}
    context_message = request.GET.get("context")
    if context_message:
        context["message"] = context_message
    return render(request, template_name="quiz/main.html", context=context)


def main_quiz(request):
    """
    Renders the main quiz page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
    return render(request, template_name="quiz/main_quiz.html")


def main_squad(request):
    """
    Renders the main squad page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
    return render(request, template_name="quiz/main_squad.html")


def result(request, quiz_type):
    """
    Renders the result page for a specific quiz.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_type (str): The type of quiz.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
    if request.method == "POST":
        # Checking type of posted quiz
        if "goalkeeper" in request.POST.keys():
            score = squad_manager.get_squad_result(quiz_type, request.POST)
        else:
            score = quiz_manager.get_quiz_result(quiz_type, request.POST.items())
    # Saving result
    user = request.user if request.user.is_authenticated else None
    result = models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    logger.debug(f"{result}")
    context = {"score": result}
    return render(request, template_name="quiz/result.html", context=context)


def profile(request, user_id):
    """
    Renders the profile page for a specific user.

    Args:
        request (HttpRequest): The HTTP request object.
        user_id (int): The ID of the user.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
    context = {
        "profile": User.objects.get(id=user_id),
        "result": models.Quiz.objects.filter(user=user_id)
        .order_by("quiz_type", "score")
        .reverse,
    }
    return render(request, template_name="quiz/profile.html", context=context)


def ranking(request, quiz_type):
    """
    Renders the ranking page for a specific quiz type or for all.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_type (str): The type of quiz.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
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
    """
    Renders the quiz page for a specific quiz type.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_type (str): The type of quiz.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
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
    """
    Renders the squad challenge page for a specific quiz type.

    Args:
        request (HttpRequest): The HTTP request object.
        quiz_type (str): The type of quiz.

    Returns:
        HttpResponse: The HTTP response containing the rendered page.

    """
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
