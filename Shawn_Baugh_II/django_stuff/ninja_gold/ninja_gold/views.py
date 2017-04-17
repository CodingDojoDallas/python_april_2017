from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    # request.session.clear()
    if 'gold' not in request.session:
        request.session['gold'] = 0
    elif 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def gold(request, location):
    print str(location)
    print request.method
    if request.method == 'POST':
        if location == 'farm':
            gold = random.randint(10,20)
        elif location == 'cave':
            gold = random.randint(5,10)
        elif location == 'house':
            gold = random.randint(2,5)
        elif location == 'casino':
            gold = random.randint(-50,50)
    else:
        return redirect('/')

    if 'gold' > 0:
        message = 'gained'
        color = 'green'
    else:
        message = 'lost'
        color = 'red'

    full_message = 'You {} {} gold from the {}'.format(message, abs(gold), location)

    message_dict = {
        'message': full_message,
        'color': color
    }
    # [{'message': 'm', 'color': 'g'},{'message': 'm', 'color': 'g'},{'message': 'm', 'color': 'g'},{'message': 'm', 'color': 'g'},]

    request.session['activities'].append(message_dict)
    request.session['gold'] += gold
    return redirect('/')
