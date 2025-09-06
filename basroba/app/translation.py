from modeltranslation.translator import register, TranslationOptions
from .models import Product

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('Product_name', 'product_description', 'Product_Category')