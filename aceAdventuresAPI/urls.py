
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('aceAPI/products/', include('products.urls')),
    path('aceAPI/customer/', include('Customer.urls')),
    path('aceAPI/order/', include('Order_func.urls'))
]
