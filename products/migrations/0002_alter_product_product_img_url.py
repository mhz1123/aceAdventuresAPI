# Generated by Django 4.1.3 on 2022-12-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img_url',
            field=models.URLField(max_length=1000),
        ),
    ]
