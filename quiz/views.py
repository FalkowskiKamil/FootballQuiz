from django.shortcuts import render
from . import data_manager
from . import models
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
        context['nation']= data_manager.get_info('nation')
        return render(request, template_name='quiz/national.html', context=context)
    
def result(request, quiz_type):
    context={'quiz_type':quiz_type}
    score=int()
    answer={}
    for key,value in request.POST.items():
        answer[key]=value
    score += data_manager.home_goal(answer['most_home_goal'])
    score += data_manager.away_goal(answer['most_away_goal'])
    score += data_manager.most_goal(answer['most_goal'])
    user = request.user if request.user.is_authenticated else None
    x= models.Quiz.objects.create(user=user, quiz_type=quiz_type, score=score)
    context['score']=x
    return render(request, template_name='quiz/result.html', context=context)