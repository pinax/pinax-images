# Usage

Add a `ForeignKey` on your content object to `ImageSet`::

    image_set = models.ForeignKey(ImageSet, blank=True, null=True)


In your view or views for creating or updating the content object, you can
capture the `pk` for the `ImageSet` that is possibly created::

    pk = request.POST.get("imageset")
    if pk and (object.image_set is None or object.image_set.pk != int(pk)):
        object.image_set = next(iter(request.user.image_sets.filter(pk=pk)), None)
    object.save()


Finally, you'll want to include a snippet like this wherever you want the panel
to appear (if you are using the associated ReactJS frontend (http://github.com/pinax/pinax-images-panel)):

    {% if image_set %}
        {% url "images_set_upload" image_set.pk as upload_url %}
    {% else %}
        {% url "images_set_new_upload" as upload_url %}
    {% endif %}
    <div id="image-panel" data-images-url="{% if image_set %}{% url "images" image_set.pk %}{% endif %}"
                          data-upload-url="{{ upload_url }}"
                          data-image-set-id="{{ image_set.pk }}">
    </div>
