# from django.db import models

# class DiscountCategory(models.Model):
#         categoryName = models.CharField(max_length=50, unique=True)
#         slug = models.SlugField(max_length = 55, unique=True)
#         categoryDescription = models.TextField(max_length=200, null=True, blank=True)
#         categoryImage = models.ImageField(upload_to='photos/dis_category', blank=True)

#         def __str__(self):
#                 return f"{self.categoryName}"



# class DiscountProduct(models.Model):
#         productName = models.CharField(max_length=40, unique=True)
#         slug = models.SlugField(max_length=45, unique=True)
#         category = models.ForeignKey(DiscountCategory, on_delete=models.CASCADE)
#         productDescription = models.TextField(max_length=200)
#         price = models.IntegerField()
#         discountPrice = models.IntegerField(blank=True, null=True)
#         productImage = models.ImageField(upload_to='photos/product')
#         stock = models.IntegerField()
#         is_available = models.BooleanField(default=True)
#         createDate = models.DateTimeField(auto_now_add = True)
#         modifiedDate = models.DateTimeField(auto_now = True)
#         def __str__(self):
#                 return f"{self.productName}"
