from django.db import models
from appStore.models import Product
from appAuth.models import User


class Cart(models.Model):
        cart_id = models.CharField(max_length=100, blank=True)
        createDate = models.DateTimeField(auto_now_add = True)
        def __str__(self):
                return f"{self.cart_id}"
        
class CartItem(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
        quantity = models.IntegerField()
        is_active = models.BooleanField(default=True)

        def sub_total(self):
                return self.product.price*self.quantity
        

        def __str__(self):
                return f"{self.product}"