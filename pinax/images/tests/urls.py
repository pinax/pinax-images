from django.urls import include, path

urlpatterns = [
    path("", include("pinax.images.urls", namespace="pinax_images")),
]
