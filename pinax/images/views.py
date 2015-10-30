from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from account.decorators import login_required


@login_required
def images(request, pk):
    image_set = get_object_or_404(request.user.image_sets.all(), pk=pk)
    return JsonResponse(image_set.image_data())


@require_POST
@login_required
def images_delete(request, pk):
    image = get_object_or_404(request.user.images.all(), pk=pk)
    image.delete()
    return JsonResponse(image.image_set.image_data())


@require_POST
@login_required
def images_make_primary(request, pk):
    image = get_object_or_404(request.user.images.all(), pk=pk)
    image.toggle_primary()
    return JsonResponse(image.image_set.image_data())


@require_POST
@login_required
def images_upload(request, pk=None):
    if pk is None:
        image_set = request.user.image_sets.create()
    else:
        image_set = get_object_or_404(request.user.image_sets.all(), pk=pk)
    for fp in request.FILES.getlist("files"):
        image_set.images.create(
            image=fp,
            original_filename=fp.name,
            created_by=request.user
        )
    return JsonResponse(image_set.image_data())
