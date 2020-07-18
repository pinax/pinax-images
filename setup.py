from setuptools import find_packages, setup

VERSION = "4.0.1"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-images.svg
    :target: https://pypi.python.org/pypi/pinax-images/

============
Pinax Images
============

.. image:: https://img.shields.io/pypi/v/pinax-images.svg
    :target: https://pypi.python.org/pypi/pinax-images/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-images.svg
    :target: https://circleci.com/gh/pinax/pinax-images
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-images.svg
    :target: https://codecov.io/gh/pinax/pinax-images
.. image:: https://img.shields.io/github/contributors/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

``pinax-images`` is a Django app for managing collections of images associated with a content object.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+
| Django / Python | 3.6 | 3.7 | 3.8 |
+=================+=====+=====+=====+
|  2.2            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
|  3.0            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="an app for managing collections of images associated with a content object",
    name="pinax-images",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-images/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "images": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=2.2",
        "django-imagekit>=4.0.2",
        "pilkit>=2.0.0",
        "pillow>=7.1.2",
        "pytz>=2020.1",
    ],
    tests_require=[
        "django-test-plus>=1.4.0",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
