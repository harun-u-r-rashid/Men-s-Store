from django.db import models
from appCategory.models import Category
from django.contrib.auth.models import User
from .constants import STAR



class Product(models.Model):
        productName = models.CharField(max_length=40, unique=True)
        slug = models.SlugField(max_length=45, unique=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        productDescription = models.TextField(max_length=200)
        price = models.IntegerField()
        productImage = models.ImageField(upload_to='photos/product')
        stock = models.IntegerField()
        is_available = models.BooleanField(default=True)
        createDate = models.DateTimeField(auto_now_add = True)
        modifiedDate = models.DateTimeField(auto_now = True)
        def __str__(self):
                return f"{self.productName}"
        

        
class Review(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        rating = models.CharField(max_length=10, choices=STAR)
        review = models.TextField(max_length=200)

        def __str__(self):
                return f"{self.product}"
        
        