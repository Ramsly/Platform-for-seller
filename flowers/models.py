from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)


class Buyer(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)


class FlowerLot(models.Model):
    CHOICE_COLOR = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Purple', 'Purple'),
    )

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="flower_lot_of_seller")
    title = models.CharField(max_length=100, default="")
    color = models.CharField(choices=CHOICE_COLOR)
    count = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    visible = models.BooleanField(default=True)


class CommentsForLots(models.Model):
    flower = models.ForeignKey(FlowerLot, on_delete=models.CASCADE)
    text = models.TextField(default="", max_length=500)


class CommentForSeller(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="comments_to_seller")
    text = models.TextField(default="", max_length=500)


class Deal(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Sold', 'Sold'),
        ('Error', 'Error')
    )

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="deal_with_seller")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="deal_with_buyer")
    flower = models.ForeignKey(FlowerLot, on_delete=models.CASCADE, related_name="deal_with_flower")
    status = models.CharField(choices=STATUS)