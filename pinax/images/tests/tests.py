from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from ..compat import mock
from ..models import Image
from .test import TestCase


class ImageSetUploadView(TestCase):

    def setUp(self):
        self.user = self.make_user("arthur")
        self.image_file = SimpleUploadedFile(
            name="foo.gif",
            content=b"GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00"
        )

        self.mock_file = mock.Mock(spec=File)
        self.mock_file.read.return_value = "fake file contents"

    def test_upload_by_anonymous(self):
        """
        Ensure anonymous user is redirected
        """
        self.get("pinax_images:imageset_new_upload")
        self.response_302()  # user should be redirected

    def test_upload_get(self):
        """
        Ensure GET action returns error code
        """
        path = reverse("pinax_images:imageset_new_upload")
        with self.login(self.user):
            self.get(path)
            self.response_405()

    def test_upload_new_imageset(self):
        """
        Upload image and store in new ImageSet.
        """
        url = "pinax_images:imageset_new_upload"
        post_data = {"files": self.image_file}
        with self.login(self.user):
            self.post(url, data=post_data)
            self.response_200()
            self.assertEqual(self.user.image_sets.count(), 1)
            self.assertEqual(self.user.images.count(), 1)
            self.assertEqual(self.user.images.get().image_set, self.user.image_sets.get())

    def test_upload_image(self):
        """
        Upload image to existing ImageSet.
        """
        image_set = self.user.image_sets.create()
        post_data = {"files": self.image_file}
        url = "pinax_images:imageset_upload"
        with self.login(self.user):
            self.post(url, image_set.pk, data=post_data)
            self.response_200()
            self.assertEqual(self.user.images.count(), 1)
            self.assertEqual(self.user.images.get().image_set, image_set)


class ImageSetMixin(object):

    def setUp(self):
        self.user = self.make_user("arthur")
        # create imageset for Arthur
        self.image_set = self.user.image_sets.create()
        # create image in imageset
        self.image = Image.objects.create(
            image_set=self.image_set,
            image=SimpleUploadedFile(
                name="foo.gif",
                content=b"GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00"
            ),
            original_filename="foo.gif",
            created_by=self.user
        )


class ImageSetDetailView(ImageSetMixin, TestCase):

    def setUp(self):
        super(ImageSetDetailView, self).setUp()
        self.view_url = "pinax_images:imageset_detail"

    def test_detail_by_anonymous(self):
        """
        Ensure anonymous user is redirected
        """
        self.get(self.view_url, self.image_set.pk)
        self.response_302()  # user should be redirected

    def test_detail_by_owner(self):
        """
        Ensure imageset owner can see image
        """
        with self.login(self.user):
            self.assertGoodView(self.view_url, self.image_set.pk)

    def test_detail_by_other(self):
        """
        Ensure any authenticated user can see image
        """
        other_user = self.make_user("other")
        with self.login(other_user):
            self.assertGoodView(self.view_url, self.image_set.pk)

    def test_detail_bad_pk(self):
        """
        Ensure 404 error with bad imageset PK
        """
        with self.login(self.user):
            self.get(self.view_url, pk=555)
            self.response_404()


class ImageDeleteView(ImageSetMixin, TestCase):

    def setUp(self):
        super(ImageDeleteView, self).setUp()
        self.view_url = "pinax_images:image_delete"

    def test_delete_by_anonymous(self):
        """
        Ensure anonymous user is redirected
        """
        self.post(self.view_url, self.image.pk)
        self.response_302()  # user should be redirected

    def test_delete_by_owner(self):
        """
        Ensure imageset owner can delete image
        """
        with self.login(self.user):
            self.post(self.view_url, self.image.pk)
            self.response_200()
            # Ensure image is not available
            self.assertFalse(Image.objects.filter(pk=self.image.pk))

    def test_delete_by_other(self):
        """
        Ensure non-owner cannot delete image
        """
        other_user = self.make_user("other")
        with self.login(other_user):
            self.post(self.view_url, self.image.pk)
            self.response_404()

    def test_delete_bad_pk(self):
        """
        Ensure POST with invalid ImageSet PK fails.
        """
        with self.login(self.user):
            self.post(self.view_url, 555)
            self.response_404()


class ImageTogglePrimaryView(ImageSetMixin, TestCase):

    def setUp(self):
        super(ImageTogglePrimaryView, self).setUp()
        self.view_url = "pinax_images:image_make_primary"

    def test_toggle_by_anonymous(self):
        """
        Ensure anonymous user is redirected
        """
        self.post(self.view_url, self.image.pk)
        self.response_302()  # user should be redirected

    def test_toggle_by_owner(self):
        """
        Ensure imageset owner can toggle primary image
        """
        # Ensure image_set does not have a primary image
        self.assertEqual(self.image_set.primary_image, None)

        with self.login(self.user):
            # Set primary image
            self.post(self.view_url, self.image.pk)
            self.response_200()

            # Ensure image is now primary image for image_set
            self.image_set.refresh_from_db()
            self.assertEqual(self.image_set.primary_image, self.image)

            # Reset primary image
            self.post(self.view_url, self.image.pk)
            self.response_200()

            # Ensure image is no longer primary image for image_set
            self.image_set.refresh_from_db()
            self.assertEqual(self.image_set.primary_image, None)

    def test_toggle_by_other(self):
        """
        Ensure non-owner cannot toggle primary image
        """
        other_user = self.make_user("other")
        with self.login(other_user):
            self.post(self.view_url, self.image.pk)
            self.response_404()

    def test_toggle_bad_pk(self):
        """
        Ensure POST with invalid Image PK fails.
        """
        with self.login(self.user):
            self.post(self.view_url, 555)
            self.response_404()
