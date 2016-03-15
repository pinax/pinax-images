Pinax Images
============

.. image:: http://slack.pinaxproject.com/badge.svg
   :target: http://slack.pinaxproject.com/

.. image:: https://img.shields.io/travis/pinax/pinax-images.svg
   :target: https://travis-ci.org/pinax/pinax-images

.. image:: https://img.shields.io/coveralls/pinax/pinax-images.svg
   :target: https://coveralls.io/r/pinax/pinax-images

.. image:: https://img.shields.io/pypi/dm/pinax-images.svg
   :target:  https://pypi.python.org/pypi/pinax-images/

.. image:: https://img.shields.io/pypi/v/pinax-images.svg
   :target:  https://pypi.python.org/pypi/pinax-images/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target:  https://pypi.python.org/pypi/pinax-images/




Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.
This collection can be found at http://pinaxproject.com.

pinax-images
-------------

``pinax-images`` is an app for managing collections of images associated with a content object.


Getting Started
----------------

Execute::

    pip install pinax-images


Add to `INSTALLED_APPS`::

    INSTALLED_APPS += ["pinax.images"]


Add to `urls.py`::

    url(r"^ajax/images/", include("pinax.images.urls")),


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


Documentation
---------------

The ``pinax-images`` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
--------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.
