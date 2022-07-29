from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)


class Buyer(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)


