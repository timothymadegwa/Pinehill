from django.shortcuts import render
from .models import Team, Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def team(request):
    team = Team.objects.all().filter(is_consultant=False).order_by('rank')
    consultants = Team.objects.all().filter(is_consultant=True).order_by('rank')
    context ={'team' : team,
            'consultants': consultants}
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
