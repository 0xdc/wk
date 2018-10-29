from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static


from .models import WellKnown
from .views import view, wkd

class ContentTypeTestCase(TestCase):
    def setUp(self):
        WellKnown.objects.create(key="testcase", value="""
            this is a multi-line
            testcase
            """)

    def test_for_plain_text(self):
        response = self.client.get( reverse("well-known:view", args=("testcase",) )  )
        self.assertEquals(response.__getitem__("Content-Type"), "text/plain")

class WKDTests(TestCase):
    def setUp(self):
        # This is the string "me" in zbase32
        self.me = "s8y7oh5xrdpu9psba3i5ntk64ohouhga"

    def test_for_wkd_static_redirect(self):
        response = self.client.get( reverse("well-known:wkd", args=(self.me,)) )
        self.assertIn("http", response.url)
        self.assertIn(
                static( '/'.join(['wk','openpgpkey','hu', self.me]) ),
                response.url,
        )
