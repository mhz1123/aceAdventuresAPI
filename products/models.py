from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, unique= True)
    product_price = models.FloatField(max_length=10, default=0)
    product_img_url = models.URLField(max_length=1000)
    product_image = models.ImageField(default= 'default.jpg')
    product_description = models.TextField(max_length=1000)
    product_feature = models.TextField(max_length=1000)
    product_spec = models.TextField(max_length=1000)
    inStock = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class SpareParts(models.Model):
    product = models.ForeignKey(Product,on_delete= models.DO_NOTHING, null=True, blank=True)
    sp_id = models.IntegerField(primary_key= True)
    sp_name = models.CharField(max_length=50)
    sp_price = models.FloatField(max_length=10, default=0)
    sp_img_url = models.URLField(max_length=100)
    inStock = models.BooleanField(default=True)

    def __str__(self):
        return self.sp_name