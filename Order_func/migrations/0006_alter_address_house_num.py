# Generated by Django 4.1.3 on 2022-12-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_func', '0005_alter_address_house_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='house_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
