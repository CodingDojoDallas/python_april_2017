from django.shortcuts import render, HttpResponse
import random



def index(request):
	print ('INDEX')

	return render(request, 'first_app/index.html')


def show(request, num):
	print ('made it to show')
	print num
	number = num
	number = int(number)

	images = [
		'https://static.pexels.com/photos/1029/landscape-mountains-nature-clouds.jpg',
		'https://static.pexels.com/photos/132037/pexels-photo-132037.jpeg',
		'https://s-media-cache-ak0.pinimg.com/originals/b5/37/90/b53790ced37581b19dcb0000bb7b358c.jpg',
		'http://www.markgray.com.au/images/gallery/large/desert-light.jpg',
		'https://d19fbfhz0hcvd2.cloudfront.net/UC/wp-content/uploads/2014/11/Landscape-Photography-Banner1.jpg'
	]
	
	if(number >=40 and number <=50):
		pic = images[-1]
		print pic
	elif(number < 40 and number >= 30):
		pic = images[0]

	elif(number < 30 and number >=20):
		pic = images[1]

	elif(number < 20 and number >=10):
		pic = images[2]

	elif(number < 10 and number >= 1 ):
		pic = images[3]
	else:
		pic = random.choice(images)


		

	context = {'url': pic}

	return render(request, 'first_app/show.html', context)







