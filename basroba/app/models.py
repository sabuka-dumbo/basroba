from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Color(models.Model):
    colorname = models.CharField(max_length=150)

    def __str__(self):
        return self.colorname

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_address", default=None)
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
    Product_color = models.ManyToManyField(Color, related_name="color10", default="")
    Product_XS = models.IntegerField(default=0)
    Product_S = models.IntegerField(default=0)
    Product_M = models.IntegerField(default=0)
    Product_L = models.IntegerField(default=0)
    Product_XL = models.IntegerField(default=0)
    Product_2Xl = models.IntegerField(default=0)
    Product_3Xl = models.IntegerField(default=0)
    Product_4Xl = models.IntegerField(default=0)
    Product_5Xl = models.IntegerField(default=0)
    Product_image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image5 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image6 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image7 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image8 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image9 = models.ImageField(upload_to='products/', blank=True, null=True)
    Product_image10 = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f"{self.Product_name}"
    
class CartItem(models.Model):
    user = models.ForeignKey(User, related_name="usercart", on_delete=models.CASCADE)
    Item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="item", default=None)
    Size = models.CharField(max_length=250, default='No')
    Color = models.CharField(max_length=250, default="No")
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} saved to cart:"
    
class FavoriteItem(models.Model):
    user = models.ForeignKey(User, related_name="userfavorite", on_delete=models.CASCADE)
    Item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="item2", default=None)

    def __str__(self):
        return f"{self.user} favorited:"
    
class Order(models.Model):
    user = models.ForeignKey(User, related_name="userorder", on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, related_name="orderitems")
    address = models.ForeignKey(Address_Info, on_delete=models.CASCADE, related_name="orderaddress", default=None)
    total_price = models.CharField(max_length=250, default='0')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"