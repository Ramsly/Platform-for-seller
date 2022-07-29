import json

from .models import Seller, Deal


def get_info() -> None:
    """
    Return info in form of a list of sellers with buyers\n
    Who bought items of seller. Also return total sum

    :return: None
    :rtype: None
    """
    sellers = Seller.objects.all()
    result = []
    for seller in sellers:
        deals = Deal.objects.filter(seller=seller)
        buyers = [deal.buyer.buyer for deal in deals]
        sum_of_deals = sum([deal.get_cost() for deal in deals])
        result.append([seller.seller, buyers, sum_of_deals])

    with open('data.json', 'w') as f:
        json.dump(result, f)