# Generated by Django 4.1.3 on 2022-12-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_customerprofile'),
        ('Order_func', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sp_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.spareparts'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_cart', 'incart'), ('order_placed', 'orderplaced'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='in_cart', max_length=20),
        ),
    ]
