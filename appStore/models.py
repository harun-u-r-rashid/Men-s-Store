from django.db import models
from appCategory.models import Category
from appAuth.models import User

from .constants import STAR



class Product(models.Model):
        productName = models.CharField(max_length=40, unique=True)
        slug = models.SlugField(max_length=45, unique=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        productDescription = models.TextField(max_length=200)
        price = models.IntegerField()
        discount=models.IntegerField(default=0)
        productImage = models.ImageField(upload_to='photos/product')
        stock = models.IntegerField()
        is_available = models.BooleanField(default=True)
        is_discount=models.BooleanField(default=False)
        is_new = models.BooleanField(default=False)
        createDate = models.DateTimeField(auto_now_add = True)
        modifiedDate = models.DateTimeField(auto_now = True)

        # def regular_price(self):
        #         return self.price
        

        def discount_price(self):
                return int(self.price)-int(self.discount)
        
        def __str__(self):
                return f"{self.productName}"


        

class Brand(models.Model):
        brandName = models.CharField(max_length=30, unique=True)
        image = models.ImageField(upload_to='photos/brand')
        def __str__(self):
                return f"{self.brandName}"
        
class Gallery(models.Model):
        image = models.ImageField(upload_to='photos/brand')
        
        
class Review(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        rating = models.CharField(max_length=10, choices=STAR)
        review = models.TextField(max_length=100)

        def __str__(self):
                return f"{self.product}"
        
        