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
]