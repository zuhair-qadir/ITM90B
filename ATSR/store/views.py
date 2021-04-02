from django.shortcuts import render
from .models import *


def store(request):
    products = Tool.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):

    context = {}
    return render(request, 'store/cart.html', context)

def companyquotes (request):
    context = {}
    return render(request, 'store/companyquotes.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
