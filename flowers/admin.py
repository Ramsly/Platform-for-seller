from django.contrib import admin
from django.db.models import Q

from .models import Buyer, Seller, TypeOfUser, FlowerLot, CommentForSeller, CommentsForLots, Deal


@admin.register(Buyer)
class BuyerModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return TypeOfUser.objects.filter(Q(is_buyers=True) & Q(is_seller=False))


admin.site.register(Seller)
admin.site.register(TypeOfUser)
admin.site.register(FlowerLot)
admin.site.register(CommentForSeller)
admin.site.register(CommentsForLots)
admin.site.register(Deal)
