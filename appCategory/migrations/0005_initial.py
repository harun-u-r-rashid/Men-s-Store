# Generated by Django 5.0.3 on 2024-08-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCategory', '0004_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('categoryDescription', models.TextField(blank=True, max_length=200, null=True)),
                ('categoryImage', models.ImageField(blank=True, upload_to='photos/category')),
            ],
        ),
    ]
