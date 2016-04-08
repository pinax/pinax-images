# Settings

The following settings allow you to specify the behavior of `pinax-images` in
your project.

Customizing thumbnail specs
---------------------------

By default `pinax-images` maintains four thumbnail specifications for thumbnail generation of uploaded images.
These specifications (shown below) are located in `pinax/images/specs.py`.

    PINAX_IMAGES_THUMBNAIL_SPEC = "pinax.images.specs.ImageThumbnail"
    PINAX_IMAGES_LIST_THUMBNAIL_SPEC = "pinax.images.specs.ImageListThumbnail"
    PINAX_IMAGES_SMALL_THUMBNAIL_SPEC = "pinax.images.specs.ImageSmallThumbnail"
    PINAX_IMAGES_MEDIUM_THUMBNAIL_SPEC = "pinax.images.specs.ImageMediumThumbnail"

You can customize thumbnailing options by creating your own specification class inheriting from `ImageSpec`:

    from imagekit import ImageSpec
    from pilkit.processors import ResizeToFit

    class MyCustomImageThumbnail(ImageSpec):
        processors = [ResizeToFit(800, 600)]
        format = "JPEG"
        options = {"quality": 90}

and overriding pinax-image specs in your application `settings.py`::

    PINAX_IMAGES_THUMBNAIL_SPEC = "{{my_app}}.specs.MyCustomImageThumbnail"

