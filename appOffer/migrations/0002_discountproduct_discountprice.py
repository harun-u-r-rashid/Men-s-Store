# Generated by Django 5.0.3 on 2024-07-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOffer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountproduct',
            name='discountPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
