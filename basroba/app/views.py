from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    all_products = Product.objects.all()

    return render(request, "index.html", {
        "all_products": all_products
    })

def products(request):
    return render(request, "products.html")

def product(request, ID):
    the_product = Product.objects.all().get(id=ID)
    return render(request, "product.html", {
        "product": the_product
    })

def cart(request):
    return render(request, "cart.html")

def favorites(request):
    return render(request, "favorites.html")

def profile(request):
    return render(request, "profile.html")