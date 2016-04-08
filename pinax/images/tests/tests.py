from django.core.urlresolvers import reverse

from .test import TestCase


class Tests(TestCase):

    def setUp(self):
        self.user = self.make_user("arthur")

    def test_get_imageset_upload(self):
        """
        Ensure GET action returns error code
        """
        path = reverse("pinax_images:imageset_new_upload")
        with self.login(self.user):
            self.get(path)
            self.response_405()

    def test_get_imageset_detail(self):
        """
        Ensure GET with invalid ImageSet PK fails.
        """
        with self.login(self.user):
            self.get("pinax_images:imageset_detail", pk=555)
            self.response_404()
