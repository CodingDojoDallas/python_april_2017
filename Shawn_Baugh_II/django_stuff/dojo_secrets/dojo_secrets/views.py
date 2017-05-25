from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Count

# Create your views here.

def index(request):
    return render(request, 'dojo_secrets/index.html')
#end index route
def process(request):
    is_valid = User.objects.validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/')
    user = User.objects.create_user(request.POST)
    User.objects.login(request, user)

    return redirect('/')
#end process route
def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['id'] = is_valid['user'].id
        return redirect('/secrets')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
        return redirect('/')

#end login route
def secrets(request):

    user = User.objects.get(id=request.session['id'])
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'dojo_secrets/secrets.html', {'user':user, 'posts':posts})
#end secrets route
def create_post(request):
    create = Post.objects.create(user = User.objects.get(id=request.session['id']), post = request.POST['post'])
    return redirect('/secrets')
#end create_post method
def like_post(request, id):
    this_user = User.objects.get(id=request.session['id'])
    this_post = Post.objects.get(id=id)
    this_post.like.add(this_user)
    # like = Post.objects.create(liked_posts__user)
    return redirect('/secrets')
# end like _post method
def delete_post(request, id):
    if request.method != 'POST':
        return redirect('/')
    else:
        post = Post.objects.filter(id=id).first()
        if post:
            post.delete()
        return redirect('/secrets')
def popular(request):
    user = User.objects.get(id=request.session['id'])
    posts = Post.objects.all().annotate(num_like=Count('like')).order_by('-num_like')[:5]
    return render(request, 'dojo_secrets/popular.html', {'user':user, 'posts':posts})
#end popular route
def logout(request):
    request.session.clear()
    return redirect('/')
