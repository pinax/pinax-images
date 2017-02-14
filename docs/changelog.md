# Change Log

## 2.0.1

* Update test matrix to include Django 1.10 and exclude Django dev branch

## 2.0.0

* Revise access permissions for some views:

  * ImageSet detail view now accessible by any authenticated user
  * Image delete view now accessible only by image owner.
  * Image "toggle primary" view now accessible only by image owner.

## 1.0.0

* Update version for Pinax 16.04 release

## 0.2.1

* Improve documentation

## 0.2.0

* Make DUA an optional requirement [PR #14](https://github.com/pinax/pinax-images/pull/14)

## 0.1.1

* add Pillow to install requires


## 0.1

* initial release
