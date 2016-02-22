from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from pinax.images.models import Image

try:
    from account.mixins import LoginRequiredMixin
except ImportError:
    from django.contrib.auth.mixins import LoginRequiredMixin


class ImagesView(LoginRequiredMixin, SingleObjectMixin, View):

    def get_object(self, queryset=None):
        return get_object_or_404(self.request.user.image_sets.all(), pk=self.kwargs.get(self.pk_url_kwarg))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return JsonResponse(self.object.image_data())


class ImageDeleteView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Image

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(self.object.image_set.image_data())


class ImageMakePrimaryView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Image

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.toggle_primary()
        return JsonResponse(self.object.image_set.image_data())


class ImageUploadView(LoginRequiredMixin, View):
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
