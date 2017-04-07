from django.shortcuts import render, redirect
import random

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
        request.session['random_num'] = "Press Generate to create a random string"
    return render(request,'main_app/index.html')

def create(request):
    request.session['attempt'] += 1
    request.session['random_num'] = random.randint(1234567890000,10000000000000)#is there a more efficient way to generate a 13-digit number?
    return redirect('/')

def reset(request):
    del request.session['attempt']
    return redirect('/')























# from django.shortcuts import render, redirect
# import random
#
# def index(request):
# 	# if 'attempt' isn't in session then we can assume this is the first time loading the page
# 	# so we can set both session['attempt'] and session['word']
# 	if not 'attempt' in request.session:
# 		request.session['attempt'] = 0
# 		request.session['word'] = 'Click Generate Button for a Random String'
# 	return render(request, 'main_app/index.html')
#
# def create(request):
# 	random_word = ''
# 	vowels = ['a','e','i','o','u','y']
# 	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
# 	for i in range(7):
# 		cons_index = random.randint(0,len(consonants)-1)
# 		random_word += consonants[cons_index]
# 		vow_index = random.randint(0,len(vowels)-1)
# 		random_word += vowels[vow_index]
# 	request.session['attempt'] += 1
# 	request.session['word'] = random_word
# 	return redirect('/')
#
# def reset(request):
# 	del request.session['attempt']
# 	del request.session['word']
# 	return redirect('/')
