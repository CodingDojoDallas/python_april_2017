from django.shortcuts import render
from models import Product

# Create your views here.
def index(request):
    print 'GETTING INDEX ROUTE'
    apple = Product.objects.create(name='apple', description='Really good', weight='1', price='1', cost_to_seller='.20', category='fruit')
    peach = Product.objects.create(name='peach', description='juicy', weight='3', price='2', cost_to_seller='.10', category='fruit')
    tv = Product.objects.create(name='Sony 4k T.V.', description='Super clear tv', weight='125', price='1100', cost_to_seller='419', category='electronics')
    print apple.description, apple.name, tv.description, tv.name, peach.description, peach.name
    return render(request, 'products/index.html')
