from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    all_products = Product.objects.all()

    return render(request, "index.html", {
        "all_products": all_products
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "auth.html")


def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Email is already registered")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=username,
            password=password,
            first_name=name
        )
        login(request, user)
        return redirect("home")

    return render(request, "auth.html")

def products(request, category_name):
    if category_name == "Bags":
        all_products = Product.objects.filter(Product_Category__categoryname="Bags")
    elif category_name == "Jacket":
        all_products = Product.objects.filter(Product_Category__categoryname="Jackets")
    elif category_name == "Accessories":
        all_products = Product.objects.filter(Product_Category__categoryname="Accessories")
    elif category_name == "all":
        all_products = Product.objects.all()
    elif Category.objects.filter(categoryname=category_name).exists():
        category = Category.objects.get(categoryname=category_name)
        all_products = Product.objects.filter(Product_Category=category)
    else:
        return redirect("index")

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
    if request.user.is_authenticated:
        cart_items = []
        if request.user.is_authenticated:
            cart_items = CartItem.objects.all().filter(user=request.user)

        return render(request, "cart.html", {
            "cart_items": cart_items
        })
    else:
        return redirect("login")

def favorites(request):
    if request.user.is_authenticated:
        user_favorites = []
        if request.user.is_authenticated:
            user_favorites = FavoriteItem.objects.filter(user=request.user)

        return render(request, "favorites.html", {
            "user_favorites": user_favorites
        })
    else:
        return redirect("login")

def profile(request):
    if request.user.is_authenticated:
        user_info = User_Info.objects.filter(user=request.user).first()
        order_info = Order.objects.filter(user=request.user).all()
        address_info = Address_Info.objects.filter(user=request.user).all()
        return render(request, "profile.html", {
            "user_info": user_info,
            "order_info": order_info,
            "address_info": address_info
            })
    else:
        return redirect("login")

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


@csrf_exempt  # only if you are sending JSON via JS; remove if using Django forms
@login_required
def save_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            first_name = data.get("first_name", "").strip()
            last_name = data.get("last_name", "").strip()
            email = data.get("email_address", "").strip()
            middle_name = data.get("middle_name", "No").strip()
            id_number = data.get("id_number", 0)
            phone_number = data.get("phone_number", 0)

            # Get or create the user info
            user_info, created = User_Info.objects.get_or_create(user=request.user)

            # Update fields
            user_info.first_name = first_name
            user_info.last_name = last_name
            user_info.email_address = email
            user_info.middle_name = middle_name
            user_info.id_number = id_number
            user_info.phone_number = phone_number
            user_info.save()

            return JsonResponse({"message": "User information saved successfully."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
@login_required
def delete_address(request):
    if request.method == "POST":
        data = json.loads(request.body)
        address_id = data.get("address_id", 0)

        address = get_object_or_404(Address_Info, id=address_id, user=request.user)
        address.delete()

        return JsonResponse({"message": "Address deleted successfully."})

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
@login_required
def add_address(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Use the exact keys sent from JS
            full_name = data.get("full_name", "").strip()
            street_address1 = data.get("street_address1", "").strip()
            street_address2 = data.get("street_address2", "").strip()
            city = data.get("city", "").strip()
            state_region = data.get("state_region", "").strip()
            zip_code = data.get("zip_code", 0)
            country = data.get("country", "").strip()
            phone_code = data.get("phone_code", 0)
            phone_number = data.get("phone_number", 0)
            additional_comment = data.get("additional_comment", "").strip()

            # Create address
            Address_Info.objects.create(
                user=request.user,
                full_name=full_name,
                street_address1=street_address1,
                street_address2=street_address2,
                city=city,
                State_Region=state_region,
                ZIP_code=zip_code,
                country=country,
                phone_code=phone_code,
                phone_number=phone_number,
                additional_comment=additional_comment
            )

            return JsonResponse({"message": "Address added successfully."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
