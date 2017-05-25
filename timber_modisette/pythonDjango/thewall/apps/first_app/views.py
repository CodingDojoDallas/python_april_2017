from django.shortcuts import render, HttpResponse
from .models import User, Message, Comment

# Create your views here.
def index(request):
	print ('INDEX')

	# user1 = User.objects.create(first_name='timber', last_name='modisette', email='mister.modistette@gmail.com', password='fucker')

	# user2 = User.objects.create(first_name='monic', last_name='modisette', email='neekneila@gmail.com', password='shitter')

	# print User.objects.all()

	# for i in User.objects.all():
	# 	print i

	# print User.objects.all()[0]

	# print User.objects.all()[0].first_name

	# user1 = User.objects.get(first_name='timber')
	# print user1
	

	# message1 = Message.objects.create(content='hello world', user=user)


	message1 = Message.objects.get(id=1)
	print message1.content
	# user = message1.user_id
	# print user.first_name
	return render(request, 'first_app/index.html')


