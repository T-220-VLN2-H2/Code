from django.db.models import Max
from core.models.user_bids import UserBids
from django.core.exceptions import ObjectDoesNotExist
from .item_service import ItemService
# TODO: whatis
from core.models.user_sales import UserSales


class BidService:
    def add_bid(self, form, user, item) -> bool:
        new_bid = form.save(commit=False)
        new_bid.user_id = user
        new_bid.item_id = item
        # TODO: don't hardcode experation or remove alltogether
        new_bid.expires = "2000-11-20 20:20"

        if item.is_sold:
            return False

        max_bid = self.get_max_bid(item)
        if max_bid is None or new_bid.amount > max_bid.amount:
            new_bid.save()
            return True

        return False

    def get_max_bid(self, item_id):
        try:
            max_bid = UserBids.objects.filter(item_id=item_id).latest("amount")
        except ObjectDoesNotExist:
            return None

        return max_bid

    def accept_bid(self, bid: UserBids):
        # TODO: auth user?
        item = bid.item_id
        item.is_sold = True
        item.save()
        # TODO: pseudo-notify buyer
        # TODO: pseudo-notify losers
