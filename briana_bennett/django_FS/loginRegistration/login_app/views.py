from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'login_app/index.html')

def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
	else:
		if check[0] == False:
			for error in check[1]:
				# messages.error(request, error)
				messages.add_message(request, messages.INFO, error, extra_tags="registration")
				return redirect('/')
		if check[0] == True:
			#create user, log them in
			#has the password
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			
			user = User.objects.create(
				first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),
				email = request.POST.get('email'),
				password = hashed_pw,
				)
			request.session['user_id'] = user.id
			# print user
			return redirect('/success')

def login(request):
	user = User.objects.filter(email = request.POST.get('email')).first()

	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/success')
	else: 
		# messages.error(request, 'invalid credentials')
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')
		
		
def success(request):
	
	user = {
		'user': User.objects.get(id = request.session['user_id'])
		}
	print user

	return render(request, 'login_app/success.html', user)

