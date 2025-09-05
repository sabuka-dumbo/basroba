from django.shortcuts import render, get_object_or_404
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
    product = get_object_or_404(Product, id=ID)

    product_images = [
        product.Product_image1,
        product.Product_image2,
        product.Product_image3,
        product.Product_image4,
        product.Product_image5,
        product.Product_image6,
        product.Product_image7,
        product.Product_image8,
        product.Product_image9,
        product.Product_image10,
    ]

    # ✅ Colors from ManyToManyField
    product_colors = product.Product_color.all()

    # Available sizes
    available_sizes = []
    size_map = {
        "XS": product.Product_XS,
        "S": product.Product_S,
        "M": product.Product_M,
        "L": product.Product_L,
        "XL": product.Product_XL,
        "2XL": product.Product_2Xl,
        "3XL": product.Product_3Xl,
        "4XL": product.Product_4Xl,
        "5XL": product.Product_5Xl,
    }
    for size, stock in size_map.items():
        if stock > 0:
            available_sizes.append(size)

    return render(request, "product.html", {
        "product": product,
        "product_images": product_images,
        "product_colors": product_colors,
        "available_sizes": available_sizes,
    })

def cart(request):
    return render(request, "cart.html")

def favorites(request):
    return render(request, "favorites.html")

def profile(request):
    return render(request, "profile.html")