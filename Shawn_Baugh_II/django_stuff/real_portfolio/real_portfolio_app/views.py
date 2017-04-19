from django.shortcuts import render, HttpResponse

# Create your views here.
# HOME/INDEX ROUTE
def index(request):
    print 'Getting index route'
    return render(request, 'real_portfolio_app/index.html')
# END INDEX ROUTE

# ABOUT ROUTE
def about(request):
    print 'Getting about route'
    return render(request, 'real_portfolio_app/about.html')
# END ABOUT ROUTE

# PROJECTS ROUTE
def projects(request):
    print 'Getting projects route'
    return render(request, 'real_portfolio_app/projects.html')
# END PROJECTS ROUTE

# TESTIMONIALS ROUTE
def testimonials(request):
    print 'Getting testimonials route'
    return render(request, 'real_portfolio_app/testimonials.html')
# END TESTIMONIALS ROUTE
