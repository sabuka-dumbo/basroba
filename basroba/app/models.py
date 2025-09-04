from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    first_name = models.CharField(max_length=150, default="No")
    middle_name = models.CharField(max_length=150, default="No")
    last_name = models.CharField(max_length=150, default="No")
    id_number = models.IntegerField(default=0)
    email_address = models.EmailField(default="No")
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s info"
    
class Address_Info(models.Model):
    full_name = models.CharField(max_length=250, default='No')
    street_address1 = models.CharField(max_length=250, default='No')
    street_address2 = models.CharField(max_length=250, default='No')
    city = models.CharField(max_length=150, default='No')
    State_Region = models.CharField(max_length=250, default='No')
    ZIP_code = models.IntegerField(default=0)
    country = models.CharField(default='No', max_length=250)
    phone_number = models.IntegerField(default=0)
    phone_code = models.IntegerField(default=0)
    additional_comment = models.CharField(max_length=250, default='No')

    def __str__(self):
        return f"Address #{self.pk}"
    
class Product(models.Model):
    Product_name = models.CharField(max_length=250, default='No')
    product_description = models.CharField(max_length=250, default='No')
    Product_Category = models.CharField(max_length=250, default='No')
    Product_price_old = models.CharField(max_length=250, default='No')
    Product_price_new = models.CharField(max_length=250, default='No')
    Product_rating = models.IntegerField(default=0)
    Product_color1 = models.CharField(max_length=250, default='No')
    Product_color2 = models.CharField(max_length=250, default='No')
    Product_color3 = models.CharField(max_length=250, default='No')
    Product_color4 = models.CharField(max_length=250, default='No')
    Product_color5 = models.CharField(max_length=250, default='No')
    Product_color6 = models.CharField(max_length=250, default='No')
    Product_color7 = models.CharField(max_length=250, default='No')
    Product_color8 = models.CharField(max_length=250, default='No')
    Product_color9 = models.CharField(max_length=250, default='No')
    Product_color10 = models.CharField(max_length=250, default='No')
    Product_XS = models.IntegerField(default=0)
    Product_S = models.IntegerField(default=0)
    Product_M = models.IntegerField(default=0)
    Product_L = models.IntegerField(default=0)
    Product_XL = models.IntegerField(default=0)
    Product_2Xl = models.IntegerField(default=0)
    Product_3Xl = models.IntegerField(default=0)
    Product_4Xl = models.IntegerField(default=0)
    Product_5Xl = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Product_name}"
    
class Favorites(models.Model):
    user = models.ForeignKey(User, related_name="userfavorites", on_delete=models.CASCADE)
    favorited = models.ManyToManyField(Product, related_name="userfavorited")

    def __str__(self):
        return f"{self.user} favorites:"
    
class CartItem(models.Model):
    user = models.ForeignKey(User, related_name="usercart", on_delete=models.CASCADE)
    Item = models.ManyToManyField(Product, related_name="cartitem")
    Size = models.CharField(max_length=250, default='No')
    Color = models.CharField(max_length=250, default="No")

    def __str__(self):
        return f"{self.user} favorites:"