from django.shortcuts import render
from . import quiz_manager
from django.contrib.auth.models import User
from . import models
# Create your views here.
def main(request):
    context = {}
    context_message = request.GET.get('context')
    if context_message:
        context['message'] = context_message
    return render(request, template_name='quiz/main.html', context=context)
    
def result(request, quiz_type):
    score=quiz_manager.get_quiz(quiz_type, request.POST.items())
    user = request.user if request.user.is_authenticated else None
    result= models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    context={'score':result}
    return render(request, template_name='quiz/result.html', context=context)

def profile(request, user_id):
    context={
        'profile': User.objects.get(id=user_id),
        'result' : models.Quiz.objects.filter(user=user_id).order_by('score').reverse
    }
    return render(request, template_name='quiz/profile.html', context=context)

def ranking(request, quiz_type):
    if quiz_type != 'All':
        context={'quiz_type':quiz_type,
                'result': models.Quiz.objects.filter(quiz_type=quiz_type).order_by('score').reverse
                }
    else:
        context={'quiz_type':"All",
                 'result': models.Quiz.objects.all().order_by('score').reverse}
    return render(request, template_name='quiz/ranking.html', context=context)

def quiz(request, quiz_type):
    data=quiz_manager.get_info(quiz_type)
    context={'quiz_type':quiz_type,
             'teams':data[0],
             'first_date':data[1],
             'last_date':data[2],
             'competition':data[3],
            'questions':data[4]}
    return render(request, template_name='quiz/quiz.html', context=context)
    