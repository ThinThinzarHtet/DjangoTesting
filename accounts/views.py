from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def customers(request):
    # return HttpResponse('about page')
    return render(request, 'accounts/customers.html')

def products(request):
    # return HttpResponse('contact pafe')
    return render(request, 'accounts/products.html')

def dashboard(request):
    # return HttpResponse('dashboard pafe')
    return render(request, 'accounts/dashboard.html')