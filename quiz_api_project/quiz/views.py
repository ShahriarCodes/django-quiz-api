from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, '<h1>ajdja</h1>', context)
