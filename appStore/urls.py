from django.urls import path
from . import views

urlpatterns = [
        path('', views.store, name='store'),
        path('category/<slug:categorySlug>/', views.store, name='productByCategory'),
        path('<slug:categorySlug>/<slug:productSlug>/', views.product_detail, name='productDetail'),  
        
]      