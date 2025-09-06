from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
        "does_user_own_product": request.user.is_authenticated and CartItem.objects.filter(user=request.user, Item=product).exists(),
        "does_user_have_in_favorites": request.user.is_authenticated and FavoriteItem.objects.filter(user=request.user, Item=product).exists(),
    })

def cart(request):
    return render(request, "cart.html")

def favorites(request):
    user_favorites = []
    if request.user.is_authenticated:
        user_favorites = FavoriteItem.objects.filter(user=request.user)

    return render(request, "favorites.html", {
        "user_favorites": user_favorites
    })

def profile(request):
    return render(request, "profile.html")

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        color = data.get("color")
        size = data.get("size")

        find_product = get_object_or_404(Product, id=product_id)

        new_cart_item = CartItem.objects.create(
            user=request.user,
            Item=find_product,
            Size=size,
            Color=color
        )
        new_cart_item.save()

        print(f"new_cart_item: {new_cart_item}")

        return JsonResponse({"message": f"Added product {product_id} to cart with color {color} and size {size}."})

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def remove_from_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")

        find_product = get_object_or_404(Product, id=product_id)

        cart_item = CartItem.objects.filter(user=request.user, Item=find_product).first()
        if cart_item:
            cart_item.delete()
            return JsonResponse({"message": f"Removed product {product_id} from cart."})
        else:
            return JsonResponse({"error": "Item not found in cart."}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def add_to_favorites(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")

        find_product = get_object_or_404(Product, id=product_id)

        new_favorite_item = FavoriteItem.objects.create(
            user=request.user,
            Item=find_product
        )
        new_favorite_item.save()

        print(f"new_favorite_item: {new_favorite_item}")

        return JsonResponse({"message": f"Added product {product_id} to favorites."})

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def remove_from_favorites(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")

        find_product = get_object_or_404(Product, id=product_id)

        favorite_item = FavoriteItem.objects.filter(user=request.user, Item=find_product).first()
        if favorite_item:
            favorite_item.delete()
            return JsonResponse({"message": f"Removed product {product_id} from favorites."})
        else:
            return JsonResponse({"error": "Item not found in favorites."}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)