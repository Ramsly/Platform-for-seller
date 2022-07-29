from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seller}'


class Buyer(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.buyer}'


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
    color = models.CharField(choices=CHOICE_COLOR, max_length=10)
    count = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class CommentsForLots(models.Model):
    flower = models.ForeignKey(FlowerLot, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="comments_from_buyers_to_lots")
    text = models.TextField(default="", max_length=500)

    def __str__(self):
        return f'{self.flower} - {self.buyer} - {self.text[:10]}...'


class CommentForSeller(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="comments_to_seller")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="comments_from_buyers_to_seller")
    text = models.TextField(default="", max_length=500)

    def __str__(self):
        return f'{self.seller} - {self.buyer} - {self.text[:10]}...'


class Deal(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Sold', 'Sold'),
        ('Error', 'Error')
    )

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="deal_with_seller")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="deal_with_buyer")
    flower = models.ForeignKey(FlowerLot, on_delete=models.CASCADE, related_name="deal_with_flower")
    count = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=10)

    def __str__(self):
        return f'{self.seller} - {self.buyer} - {self.status}'
    
    def get_cost(self):
        return self.flower.price * self.count