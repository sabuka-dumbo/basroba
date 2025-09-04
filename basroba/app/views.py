from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def product(request):
    return render(request, "product.html")

def cart(request):
    return render(request, "cart.html")

def favorites(request):
    return render(request, "favorites.html")

def profile(request):
    return render(request, "profile.html")