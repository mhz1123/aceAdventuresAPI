from django.urls import path
from . import views
urlpatterns = [
    path('getAddress/<int:pk>', views.get_address),
    path('createAddress/<int:pk>', views.create_address),
    path('updateAddress/<int:pk>', views.update_address),
    path('deleteAddress/<int:pk>', views.delete_address),
    path('createOrder/<int:uk>/<int:pk>/<int:ak>', views.create_order),
    path('createOrdersp/<int:uk>/<int:sk>/<int:ak>', views.create_order),
    path('updateOrder/<int:ok>', views.update_order),
]