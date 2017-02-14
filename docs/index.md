# Pinax Images Documentation

[Pinax](http://pinaxproject.com/pinax/) is an open source ecosystem
of reusable Django apps, themes, and starter project templates.

`pinax-images` is a reusable image collection app for Django.

## Quickstart

To install pinax-images:

    pip install pinax-images

Add `pinax.images` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        "pinax.images",
        ...
    )

`pinax-images`-specific settings can be found in the [Settings](./settings.md) document.

Add an entry to your `urls.py`:

    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),

Refer to [Usage](./usage.md) for adding image collection functionality to your application.


## Dependencies

* `django-appconf>=1.0.1`
* `django-imagekit>=3.2.7`
* `pilkit>=1.1.13`
* `pillow>=3.4.2`
* `pytz>=2016.6.1`

## Changelog

See [Changelog](./changelog.md).