# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tech(models.Model):
    tech_title = models.CharField(max_length=255)
    tech_highlight = models.TextField()
    tech_full_desc = models.TextField()
    tech_created_date = models.DateField()
    tech_published_date = models.DateTimeField()
    tech_ordering = models.IntegerField()

    def sort_highlight(self):
        if(len(self.tech_highlight) >= 100):
            return self.tech_highlight[0:100]
        else:
            return self.tech_highlight
