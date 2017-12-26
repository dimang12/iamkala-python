# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tech

# Register your models here.
class TechAdmin(admin.ModelAdmin):
    list_display = ["tech_title","sort_highlight"]


admin.site.register(Tech, TechAdmin)
