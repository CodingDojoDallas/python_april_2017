from django.shortcuts import render, HttpResponse

# Create your views here.
# INDEX ROUTE
def index(request):
    print 'Getting info in index route'
    return render(request, 'portfolio_app/index.html')
# END INFEX ROUTE
def testimonials(request):
    print 'Getting info in testimonials route'
    return render(request, 'portfolio_app/testimonials.html')
