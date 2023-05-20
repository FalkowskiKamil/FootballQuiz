from django.shortcuts import render
import pandas as pd
df = pd.read_csv("quiz/data/national/results.csv", encoding="ISO-8859-1")
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
        context['nation']= df['home_team'].unique
        return render(request, template_name='quiz/national.html', context=context)
    
def result(request, quiz_type):
    context={'quiz_type':quiz_type}
    
   
    
    home_team = df.groupby('home_team')
    home_scores=home_team['home_score'].count().sort_values(ascending=False)
    away_team = df.groupby('away_team')
    away_scores = away_team['away_score'].count().sort_values(ascending=False)    
    most_goal=(home_scores+away_scores).sort_values(ascending=False)
    answer={}
    for key,value in request.POST.items():
        answer[key]=value
    
    home_scores=home_scores[:10]
    away_scores=away_scores[:10]
    home_scores=home_scores.to_dict()
    away_scores=away_scores.to_dict()
    most_goal.to_dict()
    context['most_goal']=most_goal[:10].astype('int64')
    context['away_goal']=away_scores
    context['home_goal']= home_scores
    return render(request, template_name='quiz/result.html', context=context)