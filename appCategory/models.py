from django.db import models



class Category(models.Model):
        categoryName = models.CharField(max_length=12, unique=True)
        slug = models.SlugField(max_length = 13, unique=True)
        image = models.ImageField(upload_to='photos/category', blank=True)
        starting_price = models.IntegerField(blank=True, null=True)


        def __str__(self):
                return f"{self.categoryName}"





        