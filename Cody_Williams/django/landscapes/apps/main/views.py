from django.shortcuts import render
import random

def isPrime(n):
	n = int(n)
	i = 2
	while(i * i <= n):
		if(n % i == 0):
			return False
		i += 1
	return n > 1
# Create your views here.
def index(request, n):
	n = int(n)
	landscapes = [
		'https://photogrist.com/wp-content/uploads/2016/09/Miyamoto-Yoshihisa2.jpg',
		'https://i.ytimg.com/vi/UzhkZIOZIPI/maxresdefault.jpg',
		'http://blog.topazlabs.com/wp-content/uploads/2015/01/DSC2159-Edit.jpg',
		'http://www.visitcalifornia.com/sites/default/files/styles/welcome_image/public/CAVineyardSpring_G.Rose_%28c%29WineInstitute%282%29_1280x642_1.jpg',
		'https://drnorth.files.wordpress.com/2010/01/avatar_concept_art-3.jpg',
		'https://s-media-cache-ak0.pinimg.com/originals/bd/22/0b/bd220b10df344e654b57d514d3e506a2.jpg',
	]
	if n < 1 or n > 50:
		pic = random.choice(landscapes)
	elif isPrime(n):
		pic = landscapes[-1]	
	elif n < 11:
		pic = landscapes[0]
	elif n < 21:
		pic = landscapes[1]
	elif n < 31:
		pic = landscapes[2]
	elif n < 41:
		pic = landscapes[3]
	else:
		pic = landscapes[4]
	context = {
		'pic': pic,
	}
	return render(request, 'main/index.html', context)
