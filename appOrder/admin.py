from django.contrib import admin

from .models import Order, OrderProduct, Payment, PaymentGateway


admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Payment)
admin.site.register(PaymentGateway)



