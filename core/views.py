import os
import resend
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, ContactMessage

# Resend API Key set karein
resend.api_key = os.environ.get('RESEND_API_KEY')

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

        # 2. Resend API ke zariye direct Gmail par email bhejein
        try:
            params = {
                "from": "onboarding@resend.dev",
                "to": ["devanshgiri2004@gmail.com"],  # Aapka Gmail
                "subject": f"New Portfolio Message: {subject}",
                "html": f"""
                    <h3>New Message from Portfolio</h3>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Subject:</strong> {subject}</p>
                    <p><strong>Message:</strong><br>{message}</p>
                """,
            }
            resend.Emails.send(params)
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