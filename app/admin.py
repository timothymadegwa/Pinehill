from django.contrib import admin
from .models import Team, Job, JobApplication, Contact, TalentPool

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','is_published', 'rank','is_consultant', 'title')
    list_display_links = ('id','name', 'title')
    list_editable = ('is_consultant','is_published')
    list_filter = ('is_consultant','is_published')
    search_fields = ('name', 'email', 'title')
    list_per_page = 20

admin.site.register(Team, TeamAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','f_name', 'email','company')
    list_display_links = ('id','f_name', 'email')

admin.site.register(Contact, ContactAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published','closing')
    list_display_links = ('id','title',)
    list_editable = ('is_published',)
    search_fields = ('title',)

admin.site.register(Job, JobAdmin)

class TalentPoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    list_per_page = 25

admin.site.register(TalentPool, TalentPoolAdmin)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','job_id', 'first_name', 'last_name', 'email', 'phone')
    list_display_links = ('id', 'job_id', 'first_name', 'last_name')
    search_fields = ('job_id', 'email', 'first_name', 'last_name')
    list_per_page = 25

admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.site_header = "PineHill Website Administration"