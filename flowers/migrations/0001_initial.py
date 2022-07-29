# Generated by Django 4.0.6 on 2022-07-29 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlowerLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Purple', 'Purple')], max_length=10)),
                ('count', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flower_lot_of_seller', to='flowers.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Sold', 'Sold'), ('Error', 'Error')], max_length=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_buyer', to='flowers.buyer')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_flower', to='flowers.flowerlot')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_with_seller', to='flowers.seller')),
            ],
        ),
        migrations.CreateModel(
            name='CommentsForLots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=500)),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flowerlot')),
            ],
        ),
        migrations.CreateModel(
            name='CommentForSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=500)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_to_seller', to='flowers.seller')),
            ],
        ),
    ]