from django.db import models
from Customer.models import User
from products.models import Product, SpareParts

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.BigAutoField(primary_key=True)
    house_num = models.CharField(max_length=250,null=True, blank=True)
    street = models.CharField(max_length=250, null= True, blank=True)
    area = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    def __str__(self):
        address = self.house_num+","+self.area+","+self.city+","+self.zip_code+","+self.district+","+self.state+","+self.country
        return address

class Order(models.Model):
    ORDER_STATUS = (
        ('in_cart', 'incart'),
        ('order_placed', 'orderplaced'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,null=True, blank=True)
    sp = models.ForeignKey(SpareParts, on_delete=models.DO_NOTHING,null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total_amt = models.FloatField(default=0.0)
    order_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default= 'in_cart')
