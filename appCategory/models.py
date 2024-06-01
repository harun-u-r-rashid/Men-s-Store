from django.db import models



class Category(models.Model):
        categoryName = models.CharField(max_length=50, unique=True)
        slug = models.SlugField(max_length = 55, unique=True)
        categoryDescription = models.TextField(max_length=200, null=True, blank=True)
        categoryImage = models.ImageField(upload_to='photos/category', blank=True)

        def __str__(self):
                return f"{self.categoryName}"
        


        