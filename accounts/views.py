from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse('about page')

def contact(request):
    return HttpResponse('contact pafe')

def dashboard(request):
    return HttpResponse('dashboard pafe')