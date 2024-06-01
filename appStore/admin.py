from django.contrib import admin

from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('productName',)}

        list_display = ['productName', 'price', 'category', 'stock', 'is_available', 'createDate', 'modifiedDate']



admin.site.register(Product, ProductAdmin)
admin.site.register(Review)


