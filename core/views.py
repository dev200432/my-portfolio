from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # 1. Database mein save karein (Admin Panel ke liye)
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        # 2. Email bhejne ka code (Direct Gmail par notification ke liye)
        email_subject = f"New Portfolio Message: {subject}"
        email_message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER], # Yeh aapke Gmail par aayega
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        messages.success(request, "Aapka message successfully send ho gaya hai!")
        return redirect('home')

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })