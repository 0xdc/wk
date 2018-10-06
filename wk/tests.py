from django.test import TestCase
from django.urls import reverse

from .models import WellKnown

class ContentTypeTestCase(TestCase):
    def setUp(self):
        WellKnown.objects.create(key="testcase", value="""
            this is a multi-line
            testcase
            """)

    def test_for_plain_text(self):
        response = self.client.get( reverse("well-known:view", args=("testcase",) )  )
        self.assertEquals(response.__getitem__("Content-Type"), "text/plain")
