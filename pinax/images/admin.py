from django.contrib import admin
from django.utils.html import format_html

from .models import Image, ImageSet


class ImageInline(admin.TabularInline):
    model = Image
    fields = ["image", "created_by", "preview"]
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.pk:
            return format_html(
                f"<img src='{obj.small_thumbnail.url}' />"
            )
        return "Upload image for preview"
    preview.allow_tags = True


admin.site.register(
    ImageSet,
    list_display=["primary_image", "created_by", "created_at"],
    raw_id_fields=["created_by"],
    inlines=[ImageInline],
)
