from django.urls import path
from . import views


urlpatterns = [
        path('checkout/', views.checkout, name='checkout'),
        path('order_complete/', views.orderComplete, name='order_complete'),
        path('payment/success/', views.successView, name='success'),
        path('payment/fail/', views.failView, name='fail'),
        path('order_history/', views.orderHistory, name='history'),
        path('order_details/<int:orderId>', views.orderDetails, name='orderDetails'),
        path('payment/', views.payment, name='payment'),
        
]