from django.shortcuts import render

def index(request):
	return render(request, 'vanish_ninja_app/index.html')

# def all(request):
# 	context = {
# 		'image': 'vanish_ninja_app/images/tmnt.png'
# 	}
# 	return render(request, 'vanish_ninja_app/all.html', context)

def show(request, color):
	colors = {
		'blue': 'vanish_ninja_app/images/leonardo.jpg',
		'orange': 'vanish_ninja_app/images/michelangelo.jpg',
		'red': 'vanish_ninja_app/images/raphael.jpg',
		'purple': 'vanish_ninja_app/images/donatello.jpg',
		'tmnt': 'vanish_ninja_app/images/tmnt.png'
	}
	if color in colors:
			context = {
				'image': colors[color]
			}
	else:
		context = {
			'image' : 'vanish_ninja_app/images/notapril.jpg'
		}
	return render(request, 'vanish_ninja_app/show.html', context)