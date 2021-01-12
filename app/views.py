from django.shortcuts import render, get_object_or_404,redirect
from .models import Team, Job, JobApplication, Contact, TalentPool
from datetime import date, datetime
from django.utils import timezone
from django.contrib import messages
from smtplib import SMTP_SSL
from email.message import EmailMessage
import imghdr

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
        send_to = ['info@pinehillconsulting.co.ke']
        mail_message = f"There has been a contact on the website by {f_name} {l_name} {email} who works for {company} with the message below \n\n {message}"
        msg = EmailMessage()
        msg['Subject'] = "Contact on the Pinehill Website"
        msg['From'] = 'webadmin@pinehillconsulting.co.ke'
        msg['To'] = send_to
        msg.set_content(mail_message)
        with SMTP_SSL('mail.pinehillconsulting.co.ke' , 465) as server:
            server.login('webadmin@pinehillconsulting.co.ke', '')
            server.send_message(msg)
        message = 'Thankyou for contacting us '+f_name+', We will get back to you shortly'
        messages.success(request, message)
        return render(request, 'app/consulting.html')
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
    jobs = Job.objects.filter(is_published=True)
    context = {
        'jobs' : jobs,
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
            send_to = ['info@pinehillconsulting.co.ke', 'recruitment@pinehillconsulting.co.ke']
            mail_message = f"A Resume has been submitted to the talentpool on the website by {f_name} {l_name} {email} and phone number {phone}. Kindly check the website for further details."
            msg = EmailMessage()
            msg['Subject'] = "Resume submission to TalentPool"
            msg['From'] = 'webadmin@pinehillconsulting.co.ke'
            msg['To'] = send_to
            msg.set_content(mail_message)
            with SMTP_SSL('mail.pinehillconsulting.co.ke' , 465) as server:
                server.login('webadmin@pinehillconsulting.co.ke', '')
                server.send_message(msg)
            message = "Thank you "+f_name+" for submitting your CV"
            messages.success(request, message)
        else:
            message = f_name+" , Please ensure the files that you uploaded are in pdf format!"
            messages.error(request, message)
        return render(request, 'app/careers.html', context)
    
    return render(request, 'app/careers.html', context)

def career(request, id):
    job = get_object_or_404(Job, id=id)
    current_date = timezone.now
    context = {'job': job, 'current_date' : current_date}
    if request.method == 'POST':
        title = request.POST['job_title']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        cover_letter = request.FILES['cover']
        cv = request.FILES['cv']
        if cover_letter.name.endswith('.pdf') and cv.name.endswith('.pdf'):
            job = Job.objects.filter(title__iexact=title)[0]
            application = JobApplication(job_id=job, email=email, first_name=f_name, last_name=l_name, phone=phone, cover=cover_letter, cv=cv)
            application.save()
            send_to = ['info@pinehillconsulting.co.ke', 'recruitment@pinehillconsulting.co.ke']
            mail_message = f"A Resume has been submitted for the {title} posiition on the website by {f_name} {l_name} {email} and phone number {phone}. Kindly check the website for further details."
            msg = EmailMessage()
            msg['Subject'] = f"Application for the {title} Position."
            msg['From'] = 'webadmin@pinehillconsulting.co.ke'
            msg['To'] = send_to
            msg.set_content(mail_message)
            with SMTP_SSL('mail.pinehillconsulting.co.ke' , 465) as server:
                server.login('webadmin@pinehillconsulting.co.ke', '')
                server.send_message(msg)
            message = "Thank you "+f_name+" for submitting your application"
            messages.success(request, message)
        else:
            message = f_name+" , Please ensure the files that you uploaded are in pdf format!"
            messages.error(request, message)
        return redirect('career', id=id)
    return render(request, 'app/career.html', context)
