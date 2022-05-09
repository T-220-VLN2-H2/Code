from django.db.models import Max
from core.models.user_bids import UserBids
from django.core.exceptions import ObjectDoesNotExist
from .item_service import ItemService
from .user_service import UserService

class BidService:
    def add_bid(self, form, user, item) -> bool:
        new_bid = form.save(commit=False)
        new_bid.user_id = user
        new_bid.item_id = item
        # TODO: don't hardcode experation or remove alltogether
        new_bid.expires = "2000-11-20 20:20"
        if item.is_sold or user.id == item.seller_id:
            return False
        max_bid = self.get_max_bid(item)
        if max_bid is None or new_bid.amount > max_bid.amount:
            self.check_user_rebid(user.id, item.id)
            new_bid.save()
            return True

        return False

    @classmethod
    def check_user_rebid(cls, user, item_id):
        """
        Checks if the user has old bids on this item and removes them.
        """
        user_bids = cls.get_user_bids(user)
        for user_bid in user_bids:
            if user_bid.item_id_id == item_id:
                UserBids.objects.filter(id=user_bid.id).delete()

    @classmethod
    def get_bid_by_id(cls, bid_id):
        bid = UserBids.objects.get(id=bid_id)
        return bid

    def get_max_bid(self, item_id):
        try:
            max_bid = UserBids.objects.filter(item_id=item_id).latest("amount")
        except ObjectDoesNotExist:
            return None

        return max_bid

    @classmethod
    def accept_bid(self, bid: UserBids):
        # TODO: auth user?
        item = bid.item_id
        item.is_sold = True
        item.save()
        # TODO: pseudo-notify buyer
        # TODO: pseudo-notify losers

    @classmethod
    def get_user_bids(cls, user, active=True):
        """
        get current users bids
        """
        try:
            bids = UserBids.objects.filter(
                user_id=user, item_id__is_sold=not active
            ).order_by("-timestamp")
        except ObjectDoesNotExist:
            return None
        return bids

    @staticmethod
    def get_bids_for_user_items(user):
        bids = UserBids.objects.filter(user_id=user).order_by("-timestamp")
        user_sales = UserSales.objects.get(user_id=user)
        my_bids = []
        # TODO: Can this be optimized xD ???
        for bid in bids:
            for item in user_sales.items.all():
                if bid.item_id.id == item.id and not item.is_sold:
                    my_bids.append(bid)
        return my_bids
