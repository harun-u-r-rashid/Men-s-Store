# Generated by Django 5.0.3 on 2024-07-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0005_product_discount_product_is_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
