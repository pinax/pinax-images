from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^sets/new/upload/$", views.ImageUploadView.as_view(), name="images_set_new_upload"),
    url(r"^sets/(?P<pk>\d+)/upload/$", views.ImageUploadView.as_view(), name="images_set_upload"),
    url(r"^sets/(?P<pk>\d+)/$", views.ImagesView.as_view(), name="images"),
    url(r"^(?P<pk>\d+)/delete/$", views.ImageDeleteView.as_view(), name="images_delete"),
    url(r"^(?P<pk>\d+)/make-primary/$", views.ImageMakePrimaryView.as_view(), name="images_make_primary"),
]
