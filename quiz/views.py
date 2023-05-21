from django.shortcuts import render
from . import quiz_manager
from . import models
from .quizzes import national_quiz
# Create your views here.
def main(request):
    context = {}
    context_message = request.GET.get('context')
    if context_message:
        context['message'] = context_message
    return render(request, template_name='quiz/main.html', context=context)

def clubs(request):
    context={}
    return render(request, template_name='quiz/clubs.html', context=context)

def national(request):
    context={'quiz_type':'national'}
    if request.method=='GET':
        context['nation']= quiz_manager.get_info('nation')
        return render(request, template_name='quiz/national.html', context=context)
    
def result(request, quiz_type):
    score=quiz_manager.national(request.POST.items())
    user = request.user if request.user.is_authenticated else None
    result= models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    context={'score':result}
    return render(request, template_name='quiz/result.html', context=context)