# Generated by Django 4.1.3 on 2022-12-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='customer_phone',
            field=models.IntegerField(default=0),
        ),
    ]
