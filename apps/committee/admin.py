from django.contrib import admin
from committee.models import Member
from django.utils.html import format_html
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    def profile_image(self, obj):
        return format_html('<img src="{}" width="auto" height="150px"/>'.format(obj.image.url))
    list_display = ["sno","name","position","batch"]
    list_display_links = ["name"]
    search_fields = ["name","position","batch"]
    list_filter = ["position"]
    fieldsets = (
        ("Member Details", {
            "fields": (
                "sno","name","position","batch","image", "profile_image"
            ),
        }),
    )
    readonly_fields = ["profile_image"]