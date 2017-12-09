from django.conf.urls import url

from . import views

app_name = "pinax_images"

urlpatterns = [
    url(r"^sets/new/upload/$", views.ImageSetUploadView.as_view(), name="imageset_new_upload"),
    url(r"^sets/(?P<pk>\d+)/upload/$", views.ImageSetUploadView.as_view(), name="imageset_upload"),
    url(r"^sets/(?P<pk>\d+)/$", views.ImageSetDetailView.as_view(), name="imageset_detail"),
    url(r"^(?P<pk>\d+)/delete/$", views.ImageDeleteView.as_view(), name="image_delete"),
    url(r"^(?P<pk>\d+)/make-primary/$", views.ImageTogglePrimaryView.as_view(), name="image_make_primary"),
]
