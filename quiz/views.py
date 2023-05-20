from django.shortcuts import render

# Create your views here.
def main(request):
    context = {}
    context_message = request.GET.get('context')
    if context_message:
        context['message'] = context_message
    return render(request, template_name='quiz/main.html', context=context)