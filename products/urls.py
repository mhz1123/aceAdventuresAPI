from django.urls import path
from . import views
urlpatterns = [
    path("productList/", views.product_details),
    path('sp/<int:pk>', views.spareParts),
]