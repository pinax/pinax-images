from django.conf.urls import include, url

urlpatterns = [
    url(r"^", include("pinax.images.urls", namespace="pinax_images")),
]
