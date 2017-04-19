from django.shortcuts import render
from models import Books
# Create your views here.
def index(request):
    book1 = Books.objects.create(title='The Great Book', author='Timmy Turner', published_date='2016-03-12' ,category='Action')
    book2 = Books.objects.create(title='Beat it Up', author='Mary Swollowth', published_date='2012-11-17' ,category='You Already Know Tho')
    book3 = Books.objects.create(title='Keep Gettin It', author='Jane Taker', published_date='2017-01-04' ,category='The Down Low')
    book4 = Books.objects.create(title='In the Eye', author='John Faulkher', published_date='2011-08-22' ,category=';)')
    book5 = Books.objects.create(title='New Position', author='Amy Tries Alot', published_date='2013-05-19' ,category='Comedy')

    print book1.title, book2.title, book3.title, book4.title, book5.title
    return render (request, 'books/index.html')
