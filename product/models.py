from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):

    # categorical data
    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used"),
    )

    # contain all products informations
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # one to many
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=5000)
    condition = models.CharField(max_length=100, choices=(CONDITION_TYPE))
    price = models.DecimalField(max_digits=10, decimal_places=5)
    created = models.DateTimeField()

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product.name


    # fix name on PRODUCT section categorys
    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'




class Category(models.Model):
    # for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    # fix name on PRODUCT section categorys
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    # for product brand
    brand_name = models.CharField(max_length=50)
    
    # fix name on PRODUCT section categorys
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name










        