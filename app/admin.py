from django.contrib import admin

# Register your models here.
from .models import Team, Job

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'rank','is_consultant', 'title')
    list_display_links = ('id','name', 'title')
    list_editable = ('is_consultant',)
    list_filter = ('is_consultant',)
    search_fields = ('name', 'email', 'title')
    list_per_page = 20

admin.site.register(Team, TeamAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published','closing')
    list_display_links = ('id','title',)
    list_editable = ('is_published',)

admin.site.register(Job, JobAdmin)