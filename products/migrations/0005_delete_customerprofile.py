# Generated by Django 4.1.3 on 2022-12-06 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_customerprofile_customer_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerProfile',
        ),
    ]