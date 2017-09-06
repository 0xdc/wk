from __future__ import unicode_literals

from django.db import models

class WellKnown(models.Model):
    key = models.CharField(max_length=255,unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
