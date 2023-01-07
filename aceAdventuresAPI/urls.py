
from django.conf import settings, urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('aceAPI/products/', include('products.urls')),
    path('aceAPI/customer/', include('Customer.urls')),
    path('aceAPI/order/', include('Order_func.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
