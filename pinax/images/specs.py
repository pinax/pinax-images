from imagekit import ImageSpec
from pilkit.processors import ResizeToFit, SmartResize


class ImageThumbnail(ImageSpec):
    processors = [ResizeToFit(800, 600)]
    format = "JPEG"
    options = {"quality": 90}


class ImageListThumbnail(ImageSpec):
    processors = [SmartResize(35, 35)]
    format = "JPEG"
    options = {"quality": 75}


class ImageSmallThumbnail(ImageSpec):
    processors = [SmartResize(100, 100)]
    format = "JPEG"
    options = {"quality": 75}


class ImageMediumThumbnail(ImageSpec):
    processors = [SmartResize(400, 400)]
    format = "JPEG"
    options = {"quality": 75}
