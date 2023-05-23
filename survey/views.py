from django.shortcuts import render

# Create your views here.
def surveys(request):
    return render(request, 'survey/survey.html' )
