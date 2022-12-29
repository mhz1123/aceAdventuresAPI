# Generated by Django 4.1.3 on 2022-12-24 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_delete_customerprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('house_num', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('area', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('zip_code', models.IntegerField()),
                ('district', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('total_amt', models.FloatField(default=0.0)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('in_cart', 'incart'), ('order_placed', 'orderplaced'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='in_cart', max_length=20)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order_func.address')),
                ('sp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.spareparts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
