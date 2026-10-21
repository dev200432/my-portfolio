from django.contrib import admin
from .models import Profile, Skill, Project, ContactMessage

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')