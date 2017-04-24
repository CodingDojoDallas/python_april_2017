# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print "Hello world!"
    return render(request, "hello_world/index.html")
