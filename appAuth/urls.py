from django.urls import path, include
from . import views

urlpatterns = [
        path('social-auth/', include('social_django.urls', namespace="social")),
        path('', views.home, name='home'),
        path('account/', views.account, name='account'),
        path('register/', views.register, name = 'register'),
        path('login/', views.userLogin, name='login'),
        path('logout/', views.userLogout, name='logout'),
        path('activate/<uidb64>/<token>/', views.activate, name='activate'),
        path('resetPassword/', views.resetPassword, name='reset_password'),
        path('resetPasswordValidate/<uidb64>/<token>/', views.activate_reset_password, name='active_reset'),    
        path('update/', views.updateProfile, name='update'),  
    
]

