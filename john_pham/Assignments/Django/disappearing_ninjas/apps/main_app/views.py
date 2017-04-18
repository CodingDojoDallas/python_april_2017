from django.shortcuts import render, redirect

def index(request):
    return render(request,'main_app/index.html')

def showall(request):
    context = {
    'image':'main_app/images/tmnt.png'
    }
    return render(request, 'main_app/ninja.html', context)

def ninja(request, color):
    turtles = {
    'blue':'main_app/images/leo.jpg',
    'orange':'main_app/images/mikey.jpg',
    'red':'main_app/images/raphael.jpg',
    'purple':'main_app/images/donnie.jpg',
    }
    if color in turtles:
        context = {
        'image': turtles[color]
        }
    else:
        context = {
        'image':'main_app/images/april.jpg'
        }
    return render(request,'main_app/ninja.html', context)
