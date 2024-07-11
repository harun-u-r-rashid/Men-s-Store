from django.urls import path
from .views import discount_store

urlpatterns = [
    path('', discount_store, name='discount_store'),
    path('discount-store/<slug:category_slug>/', discount_store, name='discount_store_by_category'),
]
