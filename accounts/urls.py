from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('customers/', views.customers),
    path('products/', views.products),
]
