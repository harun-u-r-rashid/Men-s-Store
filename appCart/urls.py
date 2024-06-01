from django.urls import path

from . import views


urlpatterns = [
        path('', views.cart, name='cart'),
        path('<int:product_id>/', views.addToCart, name='addCart'),
        path('remove/<int:product_id>/', views.removeCartItem, name="removeCartItem"),
]