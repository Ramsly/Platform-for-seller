import json
import flowers.models


def get_info() -> None:
    """
    Return info in form of a list of sellers with buyers\n
    Who bought items of seller. Also return total sum

    :return: None
    :rtype: None
    """
    sellers = flowers.models.Seller.objects.all()
    result = []
    for seller in sellers:
        deals = flowers.models.Deal.objects.filter(seller=seller)
        buyers = [deal.buyer.buyer for deal in deals]
        sum_of_deals = sum([deal.get_cost() for deal in deals])
        result.append([seller.seller, buyers, sum_of_deals])
    print(json.dumps(result, default=str, indent=2))