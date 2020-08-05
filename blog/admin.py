from django.contrib import admin
from .models import ExternalBlog, Video

class ExternalBlogAdmin(admin.ModelAdmin):
    list_display = ('id','is_published', 'title', 'author')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)

admin.site.register(ExternalBlog, ExternalBlogAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','link')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)

admin.site.register(Video, VideoAdmin)
