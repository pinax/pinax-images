import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from imagekit.models import ImageSpecField


def image_upload_to(instance, filename):
    instance.original_filename = filename
    uid = str(uuid.uuid4())
    ext = filename.split(".")[-1].lower()
    return "pinax-images/image-set-{}/{}.{}".format(instance.image_set.pk, uid, ext)


class ImageSet(models.Model):
    """
    Container for a group of Images.
    """
    primary_image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="image_sets", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def image_data(self):
        return {
            "pk": self.pk,
            "primaryImage": self.primary_image.data() if self.primary_image else {},
            "images": [image.data() for image in self.images.all()],
            "upload_url": reverse("pinax_images:imageset_upload", args=[self.pk])
        }


@python_2_unicode_compatible
class Image(models.Model):
    image_set = models.ForeignKey(ImageSet, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)
    original_filename = models.CharField(max_length=500)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    thumbnail = ImageSpecField(source="image", id="pinax_images:image:thumbnail")
    list_thumbnail = ImageSpecField(source="image", id="pinax_images:image:list_thumbnail")
    small_thumbnail = ImageSpecField(source="image", id="pinax_images:image:small_thumbnail")
    medium_thumbnail = ImageSpecField(source="image", id="pinax_images:image:medium_thumbnail")

    def __str__(self):
        return self.original_filename

    def toggle_primary(self):
        if self.image_set.primary_image == self:
            self.image_set.primary_image = None
        else:
            self.image_set.primary_image = self
        self.image_set.save()

    def data(self):
        return {
            "pk": self.pk,
            "is_primary": self == self.image_set.primary_image,
            "thumbnail": self.thumbnail.url,
            "medium_thumbnail": self.medium_thumbnail.url,
            "small_thumbnail": self.small_thumbnail.url,
            "list_thumbnail": self.list_thumbnail.url,
            "filename": self.original_filename,
            "delete_url": reverse("pinax_images:image_delete", args=[self.pk]),
            "make_primary_url": reverse("pinax_images:image_make_primary", args=[self.pk])
        }
