# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.translation import activate

# Create your views here.
def index(request):
    activate('kh')
    return render(
        request,
        "home/index.html"
    )