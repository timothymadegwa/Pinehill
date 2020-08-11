from django.shortcuts import render
from .models import Team, Job, JobApplication
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def team(request):
    team = Team.objects.filter(is_consultant=False).order_by('rank').filter(is_published=True)
    consultants = Team.objects.filter(is_consultant=True).order_by('rank').filter(is_published=True)
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
    current_date = date.today()
    jobs = Job.objects.filter(is_published=True)
    context = {
        'jobs' : jobs,
        'current_date' : current_date
    }
    if request.method == 'POST':
        title = request.POST['job_title']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        cover_letter = request.POST['cover']
        cv = request.POST['cv']
        if cover_letter.endswith('.pdf') and cv.endswith('.pdf'):
            job = Job.objects.filter(title__iexact=title)[0]
            application = JobApplication(job_id=job,title=title, email=email, first_name=f_name, last_name=l_name, phone=phone, cover=cover_letter, cv=cv)
            application.save()
            success = "Thank you "+f_name+" for submitting your application"
            context['success'] = success
        else:
            error = f_name+" , Please ensure the files that you uploaded are in pdf format!"
            context['errors'] = error
            return render(request, 'app/careers.html', context)

    return render(request, 'app/careers.html', context)
