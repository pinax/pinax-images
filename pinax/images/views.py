from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from .compat import LoginRequiredMixin
from .models import Image, ImageSet


class ImageSetUploadView(LoginRequiredMixin, View):
    image_set = None

    def get_image_set(self):
        image_set_pk = self.kwargs.get("pk", None)
        if image_set_pk is None:
            return self.request.user.image_sets.create()
        return get_object_or_404(self.request.user.image_sets.all(), pk=image_set_pk)

    def post(self, request, *args, **kwargs):
        self.image_set = self.get_image_set()
        for file in request.FILES.getlist("files"):
            self.image_set.images.create(
                image=file,
                original_filename=file.name,
                created_by=request.user
            )
        return JsonResponse(self.image_set.image_data())


class ImageSetDetailView(LoginRequiredMixin, SingleObjectMixin, View):
    model = ImageSet

    def get_object(self, queryset=None):
        return get_object_or_404(
            self.request.user.image_sets.all(),
            pk=self.kwargs.get(self.pk_url_kwarg)
        )

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse(self.object.image_data())


class ImageDeleteView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Image

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(self.object.image_set.image_data())


class ImageTogglePrimaryView(LoginRequiredMixin, SingleObjectMixin, View):
    """
    Make the specified image "primary" for the ImageSet if not already,
    or reset ImageSet primary image to None if specified image is currently
    set as the primary image.
    """
    model = Image

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.toggle_primary()
        return JsonResponse(self.object.image_set.image_data())
