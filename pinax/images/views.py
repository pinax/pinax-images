from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from .compat import LoginRequiredMixin
from .models import Image, ImageSet


class ImageSetUploadView(LoginRequiredMixin, View):
    """
    Add one or more images to an ImageSet owned by current user.
    """
    model = ImageSet

    def get_queryset(self):
        """
        Return QuerySet of all ImageSets related to user.
        """
        return self.request.user.image_sets.all()

    def get_image_set(self):
        """
        Obtain existing ImageSet if `pk` is specified, otherwise
        create a new ImageSet for the user.
        """
        image_set_pk = self.kwargs.get("pk", None)
        if image_set_pk is None:
            return self.request.user.image_sets.create()
        return get_object_or_404(self.get_queryset(), pk=image_set_pk)

    def post(self, request, *args, **kwargs):
        image_set = self.get_image_set()
        for file in request.FILES.getlist("files"):
            image_set.images.create(
                image=file,
                original_filename=file.name,
                created_by=request.user
            )
        return JsonResponse(image_set.image_data())


class ImageSetDetailView(LoginRequiredMixin, SingleObjectMixin, View):
    """
    Show ImageSet information.
    """
    model = ImageSet

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse(self.object.image_data())


class UserImageMixin(LoginRequiredMixin):
    """
    Constrains user to her own Images.
    """
    def get_queryset(self):
        """
        Return QuerySet of all Images related to user.
        """
        return self.request.user.images.all()


class ImageDeleteView(UserImageMixin, SingleObjectMixin, View):
    """
    Delete the specified image.
    """
    model = Image

    def post(self, request, *args, **kwargs):
        image = self.get_object()
        image_set = image.image_set  # save for later reference
        image.delete()
        return JsonResponse(image_set.image_data())


class ImageTogglePrimaryView(UserImageMixin, SingleObjectMixin, View):
    """
    Make the specified image "primary" for it's ImageSet if not already set.
    Reset the related ImageSet primary image to None if specified image
    is currently set as primary.
    """
    model = Image

    def post(self, request, *args, **kwargs):
        image = self.get_object()
        image.toggle_primary()
        return JsonResponse(image.image_set.image_data())
