# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random


def isPrime(n):
	n = int(n)
	i = 2
	while(i*i <= n):
		if(n%i==0):
			return False
	i +=1
	return n>1




def index(request,n):
	n=int(n)
	landscapes = [
	'https://www.google.com/search?q=breathtaking+landscapes&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj8-tevi7DTAhXp34MKHWk1BzUQ_AUIBigB&biw=1536&bih=747#tbs=isz:l&tbm=isch&q=breathtaking+landscapes+snow&imgrc=LRkbkxT5ZnZFBM:&spf=747',
	'https://www.pinterest.com/explore/namib-desert/',
	'https://georgerbswakop.files.wordpress.com/2013/03/429.jpg',
	'https://georgerbswakop.files.wordpress.com/2013/03/messumb.jpg',
	'https://www.flickr.com/photos/23887338@N04/3610316118/in/photostream/',
	'https://breathtakinglandscapes.files.wordpress.com/2013/02/mount-ararat-mountains-landscapes-desert-hills-clouds-nature-rocks-breathtaking-landscapes-84-11.jpg',
	]
	if n < 1 or n > 50:
		pic = random.choice(landscapes)
	if isPrime(n):
		pic = landscapes[-1]
	elif n<11:
		pic = landscapes[0]
	elif n<21:
		pic = landscapes[1]
	elif n<31:
		pic = landscapes[2]
	elif n<41:
		pic = landscapes[3]
	else:
		pic = landscapes[4]

	context={
	 'pic':pic,
	}
	return render(request,"random_routing/index.html",context)



# Create your views here.
