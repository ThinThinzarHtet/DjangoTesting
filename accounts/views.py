from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *
# Create your views here.
def customers(request):
    # return HttpResponse('about page')
    return render(request, 'accounts/customers.html')

def products(request):
    # return HttpResponse('contact pafe')
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {
        'products' : products
    })

def dashboard(request):
    # return HttpResponse('dashboard pafe')
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total = orders.count()
    delivered = Order.objects.filter(status="delivered").count()
    pending = Order.objects.filter(status="pending").count()
    return render(request, 'accounts/dashboard.html', {
        'customers' : customers,
        'orders' : orders,
        'total' : total,
        'delivered' : delivered,
        'pending': pending
    })