# Generated by Django 5.0.3 on 2024-08-20 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAuth', '0004_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='one.jpg', upload_to='user'),
        ),
    ]
