from django.urls import path
from . import views
urlpatterns = [
    path('productList/', views.product_list),
    path('sp/<int:pk>', views.spareParts),
    path('productDetails/<int:pk>', views.product_details),
]