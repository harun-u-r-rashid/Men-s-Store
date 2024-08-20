from django.db import models
from appAuth.models import User

from appStore.models import Product
from .constants import STATUS



class Payment(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        payment_id = models.CharField(max_length=100)
        payment_method = models.CharField(max_length=100)
        amount_paid = models.IntegerField()
        status = models.CharField(max_length=100)
        createDate = models.DateTimeField(auto_now_add = True)



class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        order_number = models.CharField(max_length=100)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        phone = models.CharField(max_length=12)
        email = models.EmailField(max_length=100)
        address = models.CharField(max_length=200)
        country = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        order_total = models.FloatField()
        tax = models.FloatField()
        status = models.CharField(max_length=100, choices = STATUS, default='NEW')
        is_ordered = models.BooleanField(default=False)
        createDate = models.DateTimeField(auto_now_add = True)


class OrderProduct(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        ordered = models.BooleanField(default=False)
        ip = models.CharField(max_length=100, blank=True, null=True)
        createDate = models.DateTimeField(auto_now_add = True)

class PaymentGateway(models.Model):
        store_id = models.CharField(max_length=500, blank = True, null= True)
        store_pass = models.CharField(max_length=500, blank=True, null=True)
        
           

