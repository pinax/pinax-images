![](http://pinaxproject.com/pinax-design/patches/pinax-images.svg)

# Pinax Images

[![](https://img.shields.io/pypi/v/pinax-images.svg)](https://pypi.python.org/pypi/pinax-images/)
[![](https://img.shields.io/circleci/project/github/pinax/pinax-images.svg)](https://circleci.com/gh/pinax/pinax-images)
[![](https://img.shields.io/codecov/c/github/pinax/pinax-images.svg)](https://codecov.io/gh/pinax/pinax-images)
[![](https://img.shields.io/github/contributors/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-images.svg)](https://github.com/pinax/pinax-images/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
  * [Dependencies](#dependencies)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## Table of Contents

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

## pinax-images

### Overview

`pinax-images` is an app for managing collections of images associated with any content object.

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *

#### Dependencies

* `django-appconf>=1.0.1`
* `django-imagekit>=3.2.7`
* `pilkit>=1.1.13`
* `pillow>=3.0`
* `pytz>=2015.6`

## Documentation

### Installation

To install pinax-images:

    pip install pinax-images

Add `pinax.images` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = (
    # other apps
    "pinax.images",
)
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

```djangotemplate
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

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
