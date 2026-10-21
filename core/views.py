from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, ContactMessage

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        messages.success(request, "Aapka message receive ho gaya hai!")
        return redirect('home')

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })