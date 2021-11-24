![](http://pinaxproject.com/pinax-design/patches/pinax-images.svg)

# Pinax Images

[![](https://img.shields.io/pypi/v/pinax-images.svg)](https://pypi.python.org/pypi/pinax-images/)

[![Build](https://github.com/pinax/pinax-images/actions/workflows/ci.yaml/badge.svg)](https://github.com/pinax/pinax-images/actions)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-images.svg)](https://codecov.io/gh/pinax/pinax-images)
[![](https://img.shields.io/github/contributors/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Dependencies](#dependencies)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-images

### Overview

`pinax-images` is an app for managing collections of images associated with any content object.

#### Dependencies

* `django-appconf>=1.0.1`
* `django-imagekit>=3.2.7`
* `pilkit>=1.1.13`
* `pillow>=3.3.0`
* `pytz>=2016.6.1`

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8 | 3.9 | 3.10
--------------- | --- | --- | --- | --- | ----
2.2  |  *  |  *  |  *  | *  |  *
3.2  |  *  |  *  |  *  | *  |  *


## Documentation

### Installation

To install pinax-images:

```shell
    $ pip install pinax-images
```

Add `pinax.images` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # other apps
    "pinax.images",
]
```

`pinax-images`-specific settings can be found in the [Settings](#settings) section.

Add `pinax.images.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    ]
```

### Usage

Adding image collection functionality to your application!

First, add a `OneToOneField` on your content object to `ImageSet`::

```python
from pinax.images.models import ImageSet

class YourModel():
    # other fields
    image_set = models.OneToOneField(ImageSet)
```

In your view for creating your content object, you should create a
new ImageSet for each new content object:

```python
class ObjectCreateView(CreateView):

    def form_valid(self, form):
        form.instance.image_set = ImageSet.objects.create(created_by=self.request.user)
        return super(CloudSpottingCreateView, self).form_valid(form)
```

Finally, you'll want to include a snippet like this wherever you want the image panel
to appear (if you are using the associated [pinax-images-panel](http://github.com/pinax/pinax-images-panel) ReactJS frontend):

```django
{% if image_set %}
    {% url "pinax_images:imageset_upload" image_set.pk as upload_url %}
{% else %}
    {% url "pinax_images:imageset_new_upload" as upload_url %}
{% endif %}
<div id="image-panel" data-images-url="{% if image_set %}{% url "pinax_images:imageset_detail" image_set.pk %}{% endif %}"
                        data-upload-url="{{ upload_url }}"
                        data-image-set-id="{{ image_set.pk }}">
</div>
```

### Settings

The following settings allow you to specify the behavior of `pinax-images` in
your project.

#### Customizing Thumbnail Specs

By default `pinax-images` maintains four thumbnail specifications for thumbnail generation of uploaded images.
These specifications (shown below) are located in `pinax/images/specs.py`.

```python
PINAX_IMAGES_THUMBNAIL_SPEC = "pinax.images.specs.ImageThumbnail"
PINAX_IMAGES_LIST_THUMBNAIL_SPEC = "pinax.images.specs.ImageListThumbnail"
PINAX_IMAGES_SMALL_THUMBNAIL_SPEC = "pinax.images.specs.ImageSmallThumbnail"
PINAX_IMAGES_MEDIUM_THUMBNAIL_SPEC = "pinax.images.specs.ImageMediumThumbnail"
```

You can customize thumbnailing options by creating your own specification class inheriting from `ImageSpec`:

```python
from imagekit import ImageSpec
from pilkit.processors import ResizeToFit

class MyCustomImageThumbnail(ImageSpec):
    processors = [ResizeToFit(800, 600)]
    format = "JPEG"
    options = {"quality": 90}
```

and overriding pinax-image specs in your application `settings.py`::

```python
PINAX_IMAGES_THUMBNAIL_SPEC = "{{my_app}}.specs.MyCustomImageThumbnail"
```

## Change Log

### 5.0.0

* Add Python 3.9 and 3.10 support along with Django 3.2
* Droppped Django 3.1
* Handled deprecation and some general modernizations
* Updated packaging

### 4.0.1

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 3.0.2

* Use format_html() to escape html tags in admin preview

### 3.0.1

* Standardize documentation, badges
* Remove django-appconf from setup.py `install_requires`
* Add third-party libs for isort-ing
* Add trove classifiers

### 3.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 2.2.0

* Move documentation to README.md
* Change `upload_to` path to have the image set PK

### 2.1.0

* Only how thumbnail if one exists

### 2.0.0

* Revise access permissions for some views:

  * ImageSet detail view now accessible by any authenticated user
  * Image delete view now accessible only by image owner.
  * Image "toggle primary" view now accessible only by image owner.

### 1.0.0

* Update version for Pinax 16.04 release

### 0.2.1

* Improve documentation

### 0.2.0

* Make DUA an optional requirement [PR #14](https://github.com/pinax/pinax-images/pull/14)

### 0.1.1

* add Pillow to install requires

### 0.1

* initial release


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
