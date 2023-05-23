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

def clubs(request):
    context={'quiz_type':'clubs'}
    data=quiz_manager.get_info('clubs')
    context['clubs_all'] = data[0]
    context['date'] = data[1:3]
    context['competition'] = data[3]
    return render(request, template_name='quiz/clubs.html', context=context)

def national(request):
    context={'quiz_type':'national'}
    data = quiz_manager.get_info('national')
    context['nation'] = data[0]
    context['date'] = data[1:]
    return render(request, template_name='quiz/national.html', context=context)
    
def result(request, quiz_type):
    score=quiz_manager.get_quiz(quiz_type, request.POST.items())
    user = request.user if request.user.is_authenticated else None
    result= models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    context={'score':result}
    return render(request, template_name='quiz/result.html', context=context)

def profile(request, user_id):
    context={
        'profile': User.objects.get(id=user_id),
        'result_national' : models.Quiz.objects.filter(user=user_id, quiz_type='national')
    }
    return render(request, template_name='quiz/profile.html', context=context)

def ranking(request, quiz_type):
    context={'quiz_type':quiz_type,
             'result': models.Quiz.objects.filter(quiz_type=quiz_type).order_by('score')
            }
    return render(request, template_name='quiz/ranking.html', context=context)