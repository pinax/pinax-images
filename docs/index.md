# pinax-images

`pinax-images` is a image collection app for Django.

!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-images

Add `pinax.images` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.images",
        # ...
    )

Add an entry to your `urls.py`:

    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),


## Dependencies

* `django-appconf>=1.0.1`
* `django-imagekit>=3.2.7`
* `pilkit>=1.1.13`
* `pillow>=3.0`
* `pytz>=2015.6`
