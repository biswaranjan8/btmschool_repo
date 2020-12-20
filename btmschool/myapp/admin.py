from django.contrib import admin
from .models import *


@admin.register(imagefiled)
class imageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(newspage)
class newsadmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'body', 'publish_date']