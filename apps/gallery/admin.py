from django.contrib import admin
from gallery.models import PhotoLink

# Register your models here.
@admin.register(PhotoLink)
class PhotoLinkAdmin(admin.ModelAdmin):
    list_display = ["title","url","date","is_visible"]