from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Favorites, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    all_products = Product.objects.all()

    return render(request, "index.html", {
        "all_products": all_products
    })

def products(request):
    return render(request, "products.html")

def product(request, ID):
    # Get the product
    product = get_object_or_404(Product, id=ID)

    # Collect all product images
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
    # Remove None values
    product_images = [img for img in product_images if img]

    # Get colors from ManyToManyField
    product_colors = product.Product_color.all()
    print(product_colors)

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

    # Render template
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

@login_required
def add_to_favorites(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        favorites, created = Favorites.objects.get_or_create(user=request.user)

        if product in favorites.favorited.all():
            favorites.favorited.remove(product)
            return JsonResponse({"status": "removed"})
        else:
            favorites.favorited.add(product)
            return JsonResponse({"status": "added"})
    return JsonResponse({"status": "error"})


@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        size = request.POST.get("size", "No")
        color = request.POST.get("color", "No")

        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            Item=product,
            Size=size,
            Color=color
        )
        cart.items.add(cart_item)
        return JsonResponse({"status": "added"})
    return JsonResponse({"status": "error"})