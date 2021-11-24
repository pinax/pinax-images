from django.urls import path

from . import views

app_name = "pinax_images"

urlpatterns = [
    path("sets/new/upload/", views.ImageSetUploadView.as_view(), name="imageset_new_upload"),
    path("sets/<int:pk>/upload/", views.ImageSetUploadView.as_view(), name="imageset_upload"),
    path("sets/<int:pk>/", views.ImageSetDetailView.as_view(), name="imageset_detail"),
    path("<int:pk>/delete/", views.ImageDeleteView.as_view(), name="image_delete"),
    path("<int:pk>/make-primary/", views.ImageTogglePrimaryView.as_view(), name="image_make_primary"),
]
