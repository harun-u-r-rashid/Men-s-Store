# Generated by Django 5.0.3 on 2024-07-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('categoryDescription', models.TextField(blank=True, max_length=200, null=True)),
                ('categoryImage', models.ImageField(blank=True, upload_to='photos/dis_category')),
            ],
        ),
    ]