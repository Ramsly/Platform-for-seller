# Generated by Django 4.0.6 on 2022-07-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0014_alter_buyer_is_buyers_alter_seller_is_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='is_buyers',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='seller',
            name='is_seller',
            field=models.BooleanField(),
        ),
    ]
