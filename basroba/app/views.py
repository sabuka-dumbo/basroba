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
    all_products = Product.objects.all()

    return render(request, "products.html", {
        "all_products": all_products
    })

def product(request, ID):
    product = get_object_or_404(Product, id=ID)
    product_images = [img for img in [
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
    ] if img]

    product_colors = product.Product_color.all()

    available_sizes = [size for size, stock in {
        "XS": product.Product_XS,
        "S": product.Product_S,
        "M": product.Product_M,
        "L": product.Product_L,
        "XL": product.Product_XL,
        "2XL": product.Product_2Xl,
        "3XL": product.Product_3Xl,
        "4XL": product.Product_4Xl,
        "5XL": product.Product_5Xl,
    }.items() if stock > 0]

    return render(request, "product.html", {
        "product": product,
        "product_images": product_images,
        "product_colors": product_colors,
        "available_sizes": available_sizes,
    })

def cart(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.all().filter(user=request.user)

    return render(request, "cart.html", {
        "cart_items": cart_items
    })

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
        if not request.user.is_authenticated:
            return JsonResponse({"error": "You must be logged in"}, status=403)

        data = json.loads(request.body)
        product_id = data.get("product_id")
        color = data.get("color")
        size = data.get("size")

        product = get_object_or_404(Product, id=product_id)

        # Check if variant exists
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            Item=product,
            Size=size,
            Color=color,
            defaults={"count": 1}
        )

        if not created:
            cart_item.count += 1
            cart_item.save()
            return JsonResponse({"message": f"Quantity updated for {size} {color}.", "in_cart": True})
        return JsonResponse({"message": f"{size} {color} added to cart.", "in_cart": True})

    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def remove_from_cart(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "You must be logged in"}, status=403)

        data = json.loads(request.body)
        product_id = data.get("product_id")
        color = data.get("color")
        size = data.get("size")

        product = get_object_or_404(Product, id=product_id)

        cart_item = CartItem.objects.filter(
            user=request.user,
            Item=product,
            Size=size,
            Color=color
        ).first()

        if cart_item:
            cart_item.delete()
            return JsonResponse({"message": f"{size} {color} removed from cart.", "in_cart": False})
        else:
            return JsonResponse({"error": "Item not in cart."}, status=404)

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

@csrf_exempt
def update_cart_count(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart_item_id = data.get("cart_item_id")
        new_count = data.get("count")

        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.count = new_count
        cart_item.save()

        return JsonResponse({"message": f"Cart item {cart_item_id} count updated to {new_count}."})

    return JsonResponse({"error": "Invalid request"}, status=400)


from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def check_variant_status(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        color = data.get("color")
        size = data.get("size")

        product = get_object_or_404(Product, id=product_id)

        in_cart = CartItem.objects.filter(user=request.user, Item=product, Size=size, Color=color).exists()
        in_fav = FavoriteItem.objects.filter(user=request.user, Item=product).exists()

        return JsonResponse({"in_cart": in_cart, "in_favorites": in_fav})
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
@login_required
def check_favorite_status(request):
    """
    Returns whether the current product is in the user's favorites
    """
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        in_favorites = FavoriteItem.objects.filter(user=request.user, Item=product).exists()
        return JsonResponse({"in_favorites": in_favorites})

    return JsonResponse({"error": "Invalid request"}, status=400)
