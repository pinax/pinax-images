from django.conf.urls import patterns, url

from .views import (
    images,
    images_upload,
    images_delete,
    images_make_primary
)


urlpatterns = patterns(
    "",
    url(r"^sets/new/upload/$", images_upload, name="images_set_new_upload"),
    url(r"^sets/(?P<pk>\d+)/upload/$", images_upload, name="images_set_upload"),
    url(r"^sets/(?P<pk>\d+)/$", images, name="images"),
    url(r"^(?P<pk>\d+)/delete/$", images_delete, name="images_delete"),
    url(r"^(?P<pk>\d+)/make-primary/$", images_make_primary, name="images_make_primary"),
)
