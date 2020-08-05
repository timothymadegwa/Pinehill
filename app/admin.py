from django.contrib import admin

# Register your models here.
from .models import Team, Contact

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'rank','is_consultant', 'title')
    list_display_links = ('id','name', 'title')
    list_editable = ('is_consultant',)
    list_filter = ('is_consultant',)
    search_fields = ('name', 'email', 'title')
    list_per_page = 20

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'message', 'contact_date')

admin.site.register(Team, TeamAdmin)
admin.site.register(Contact, ContactAdmin)