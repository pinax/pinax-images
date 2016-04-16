# Usage

First, add a `OneToOneField` on your content object to `ImageSet`::

    from pinax.images.models import ImageSet

    class YourModel():
        ...
        image_set = models.OneToOneField(ImageSet)
        ...

In your view for creating your content object, you should create a
new ImageSet for each new content object:

    class ObjectCreateView(CreateView):

        def form_valid(self, form):
            form.instance.image_set = ImageSet.objects.create(created_by=self.request.user)
            return super(CloudSpottingCreateView, self).form_valid(form)

Finally, you'll want to include a snippet like this wherever you want the image panel
to appear (if you are using the associated [pinax-images-panel](http://github.com/pinax/pinax-images-panel) ReactJS frontend):

    {% if image_set %}
        {% url "pinax_images:imageset_upload" image_set.pk as upload_url %}
    {% else %}
        {% url "pinax_images:imageset_new_upload" as upload_url %}
    {% endif %}
    <div id="image-panel" data-images-url="{% if image_set %}{% url "pinax_images:imageset_detail" image_set.pk %}{% endif %}"
                          data-upload-url="{{ upload_url }}"
                          data-image-set-id="{{ image_set.pk }}">
    </div>
