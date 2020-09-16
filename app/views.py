from django.shortcuts import render, get_object_or_404,redirect
from .models import Team, Job, JobApplication, Contact, TalentPool
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def consulting(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(f_name=f_name, l_name=l_name, company=company, email=email, phone=phone, message=message)
        contact.save()
        context = {
            'message' : f_name + ', Thankyou for contacting us, We will get back to you shortly'
        }
        return render(request, 'app/consulting.html', context)
    return render(request, 'app/consulting.html')

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

def research(request):
    return render(request, 'app/research.html')

def capacity(request):
    return render(request, 'app/capacity.html')

def hr(request):
    return render(request, 'app/hr.html')

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
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        cv = request.FILES['cv']
        
        if cv.name.endswith('.pdf'):
            talent = TalentPool(email=email, first_name=f_name, last_name=l_name, phone=phone, cv=cv)
            talent.save()
            success = "Thank you "+f_name+" for submitting your CV"
            context['success'] = success
        else:
            error = f_name+" , Please ensure the files that you uploaded are in pdf format!"
            context['errors'] = error
        return render(request, 'app/careers.html', context)
    
    return render(request, 'app/careers.html', context)

def career(request, id):
    job = get_object_or_404(Job, id=id)
    current_date = date.today()
    context = {'job': job, 'current_date' : current_date}
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
            application = JobApplication(job_id=job, email=email, first_name=f_name, last_name=l_name, phone=phone, cover=cover_letter, cv=cv)
            application.save()
            success = "Thank you "+f_name+" for submitting your application"
            context['success'] = success
        else:
            error = f_name+" , Please ensure the files that you uploaded are in pdf format!"
            context['errors'] = error
        return redirect('career', id=id)
    return render(request, 'app/career.html', context)

def events(request):
    return render(request, 'app/events.html')

def event(request, slug):
    return render(request, 'app/event.html')