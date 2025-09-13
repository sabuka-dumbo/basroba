from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path("", views.index, name='index'),
    path("products/<str:category_name>", views.products, name="products"),
    path("product/<int:ID>", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("profile/", views.profile, name="profile"),
    path("favorites/", views.favorites, name="favorites"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("aboutus/", views.aboutus_view, name="aboutus"),
    path("contactus/", views.contactus_view, name="contactus"),
    path('choose_language/', views.choose_language, name='choose_language'),
    path('set_language/', set_language, name='set_language'),

    # API endpoints
    path("api/add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("api/remove_from_cart/", views.remove_from_cart, name="remove_from_cart"),

    path("api/add_to_favorites/", views.add_to_favorites, name="add_to_favorites"),
    path("api/remove_from_favorites/", views.remove_from_favorites, name="remove_from_favorites"),

    path('update_cart_count/', views.update_cart_count, name='update_cart_count'),
    path("api/check_variant_status/", views.check_variant_status, name="check_variant_status"),
    path("api/check_favorite_status/", views.check_favorite_status, name="check_favorite_status"),

    path("api/save_user/", views.save_user, name="save_user"),

    path("api/delete_address/", views.delete_address, name="delete_address"),
    path("api/add_address/", views.add_address, name="add_address"),
    path("api/change_address1/", views.change_address1, name="change_address1"),
    path("api/change_address22/", views.change_address2, name="change_address2"),
]