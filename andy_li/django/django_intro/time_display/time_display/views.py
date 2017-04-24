# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
import time

def index(request):
    print "-= Reached / (index.html) =-"
    data = {
        "date": datetime.now().strftime("%b %d, %Y"),
        "time": time.strftime("%I:%M %p"),
    }

    return render(request, "time_display/index.html", data)
