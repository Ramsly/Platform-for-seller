# Generated by Django 4.0.6 on 2022-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0012_seller_buyer_alter_commentforseller_buyer_and_more'),
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