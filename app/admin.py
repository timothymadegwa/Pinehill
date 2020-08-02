from django.contrib import admin

# Register your models here.
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'is_consultant', 'title')
    list_editable = ('is_consultant',)
    list_filter = ('is_consultant',)
    search_fields = ('name', 'email', 'title')
    list_per_page = 20

admin.site.register(Team, TeamAdmin)