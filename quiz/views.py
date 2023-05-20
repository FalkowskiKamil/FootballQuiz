from django.shortcuts import render
import pandas as pd

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
    context={}
    if request.method=='GET':
        csv_file = pd.read_csv("quiz/data/national/results.csv", encoding="ISO-8859-1")
        context['nation']= csv_file['home_team'].unique
        return render(request, template_name='quiz/national.html', context=context)