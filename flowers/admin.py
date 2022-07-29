from django.contrib import admin

from .models import Buyer, Seller, FlowerLot, CommentForSeller, CommentsForLots, Deal

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(FlowerLot)
admin.site.register(CommentForSeller)
admin.site.register(CommentsForLots)
admin.site.register(Deal)
