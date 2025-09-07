from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.products, name="products"),
    path("product/<int:ID>", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("profile/", views.profile, name="profile"),
    path("favorites/", views.favorites, name="favorites"),

    # API endpoints
    path("api/add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("api/remove_from_cart/", views.remove_from_cart, name="remove_from_cart"),

    path("api/add_to_favorites/", views.add_to_favorites, name="add_to_favorites"),
    path("api/remove_from_favorites/", views.remove_from_favorites, name="remove_from_favorites"),

    path('update_cart_count/', views.update_cart_count, name='update_cart_count'),
    path("api/check_variant_status/", views.check_variant_status, name="check_variant_status"),
    path("api/check_favorite_status/", views.check_favorite_status, name="check_favorite_status"),

    path("api/save_user/", views.save_user, name="save_user"),
]