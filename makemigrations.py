#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings

DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "pinax.images",
        "pinax.images.tests"
    ],
    MIDDLEWARE=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    ROOT_URLCONF="pinax.images.tests.urls",
    SECRET_KEY="notasecret",
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
)


def run(*args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.core.management.call_command(
        "makemigrations",
        "pinax_images",
        *args
    )


if __name__ == "__main__":
    run(*sys.argv[1:])
