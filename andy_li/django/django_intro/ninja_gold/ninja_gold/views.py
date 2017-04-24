# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

def index(request):
    print "-= Reached / (index.html) =-"
    if "gold_ttl" and "msgs" not in request.session:
        request.session["gold_ttl"] = 0
        request.session["msgs"] = []

    return render(request, "ninja_gold/index.html")

def process(request, clicked_bldg):
    print "-= Reached /process_money/<clicked_bldg> (redirect to /) =-"
    if clicked_bldg == "farm":
        gold = random.randint(10, 20)
        request.session["gold_ttl"] += gold
    elif clicked_bldg == "cave":
        gold = random.randint(5, 10)
        request.session["gold_ttl"] += gold
    elif clicked_bldg == "house":
        gold = random.randint(2, 5)
        request.session["gold_ttl"] += gold
    elif clicked_bldg == "casino":
        gold = random.randint(-50, 50)
        request.session["gold_ttl"] += gold

    msg_dict = {}
    if gold >= 0:
        result = "Earned"
        msg_dict["color"] = "green"
    elif gold < 0:
        result = "Lost"
        msg_dict["color"] = "red"

    msg_str = "{} {} gold from the {}!".format(result, abs(gold), clicked_bldg)
    msg_dict["msg"] = msg_str
    request.session["msgs"].insert(0, msg_dict)

    return redirect("/")


def reset(request):
    print "-= Reached /reset (redirect to /) =-"
    request.session.clear()
    return redirect("/")
