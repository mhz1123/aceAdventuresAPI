# Generated by Django 4.1.3 on 2022-12-28 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order_func', '0003_remove_order_product_id_remove_order_sp_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='address',
        ),
    ]