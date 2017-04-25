from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Entry(models.Model):
    creation_date = models.DateTimeField('date Created')
    page_name = models.CharField(max_length=64)
    line_number = models.CharField(max_length=5)
    working_on = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    def __str__(self):
        return str(self.creation_date.strftime("%b %d %Y %H:%M"))
