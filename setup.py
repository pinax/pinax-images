import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Developers",
    author_email="developers@pinaxproject.com",
    description="an app for managing collections of images associated with a content object",
    name="pinax-images",
    long_description=read("README.md"),
    version="2.2.0",
    url="http://github.com/pinax/pinax-images/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "images": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "django-test-plus>=1.0.11",
        "mock>=2.0.0",
    ],
    install_requires=[
        "django-appconf>=1.0.1",
        "django-imagekit>=3.2.7",
        "pilkit>=1.1.13",
        "pillow>=3.3.0",
        "pytz>=2016.6.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
