# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Tech
from django.utils.translation import activate

# Create your views here.
def index(request):

    techs = Tech.objects.all()[:6]
    print(techs[0].tech_title)
    return render(
        request,
        "home/index.html",
        {
            "techs": techs,
            "main_tech": techs[0]

        }
    )


def techDetail(request, id):
    print(id)
    return render(
        request,
        "tech/tect-detail.html"
    )