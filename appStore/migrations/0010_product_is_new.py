# Generated by Django 5.0.3 on 2024-08-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0009_heroarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
