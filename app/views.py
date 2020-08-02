from django.shortcuts import render
from .models import Team

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def team(request):
    team = Team.objects.all()
    context ={
        'team' : team
    }
    return render(request, 'app/team.html', context)

def investment(request):
    return render(request, 'app/investment.html')

def risk(request):
    return render(request, 'app/risk.html')

def strategy(request):
    return render(request, 'app/strategy.html')

def capacity(request):
    return render(request, 'app/capacity.html')

def media(request):
    return render(request, 'app/media.html')

def careers(request):
    return render(request, 'app/careers.html')

def contact(request):
    return render(request, 'app/contact.html')
