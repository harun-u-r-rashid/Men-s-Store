
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appAuth.urls')),
    path('carts/', include('appCart.urls')),
    path('store/', include('appStore.urls')),
    path('orders/', include('appOrder.urls')),
    

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
