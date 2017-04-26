from django.shortcuts import render,redirect
import math
from random import randint
import random
# Create your views here.

def index(request):
  	return render(request, 'landscapes_app/index.html')

def show(request, num):
	print '*'*50
	num = int(num)
	print num

	images = [
		{'snow' : 'http://eskipaper.com/images/snow-landscape-2.jpg',
		'dessert' : 'http://cdn.touropia.com/gfx/d/amazing-desert-landscapes/the_pinnacles_desert.jpg',
		'forest' :	'http://kingofwallpapers.com/forest-landscape-wallpaper/forest-landscape-wallpaper-001.jpg',
		'vineyard' : 'https://s-media-cache-ak0.pinimg.com/originals/20/62/e2/2062e2fdd2e81ce97bba2e39db9ac891.jpg',
		'tropical' : 'http://www.junglemusic.net/images/PaDr54[1].jpg'},
	]

	# print(is_prime(num))

	if num>0 and num<=50:
		print is_prime(num)
		if is_prime(num) == True:
			key = random.choice(list(images[0].keys()))
			pic = images[0][key]

		else:
			if num>=1 and num<=10:
				pic = images[0]['snow']
				print pic

			elif num>=11 and num<=20:
				pic = images[0]['dessert']

			elif num>=21 and num<=30:
				pic = images[0]['forest']

			elif num>=31 and num<=40:
				pic = images[0]['vineyard']

			elif num>40 and num<=50:
				pic = images[0]['tropical']

		context = {
			'pic' : pic,
		}

		return render(request, 'landscapes_app/show.html', context)
	else:
		return redirect('/')

def is_prime(n):
	if n%2 == 0 and n>2:
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if n%i ==0:
			return False
	return True





