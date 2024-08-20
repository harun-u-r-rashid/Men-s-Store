# Generated by Django 5.0.3 on 2024-08-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCategory', '0007_remove_category_categorydescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/category'),
        ),
        migrations.AddField(
            model_name='category',
            name='starting_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]