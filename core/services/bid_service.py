from core.models.item import Item
from core.services.notification_service import NotificationService
from django.db.models import Max, Q
from core.models.user_bids import UserBids
from django.core.exceptions import ObjectDoesNotExist


class BidService:
    @classmethod
    def add_bid(cls, form, user, item) -> bool:
        new_bid = form.save(commit=False)
        new_bid.user_id = user
        new_bid.item_id = item
        # TODO: don't hardcode experation or remove alltogether
        new_bid.expires = "2000-11-20 20:20"
        if item.is_sold:
            return False

        max_bid = cls.get_max_bid(item)
        if max_bid is None or new_bid.amount > max_bid.amount:
            cls.check_rebid(user, item.id)
            new_bid.save()
            NotificationService.add_notification(
                user,
                "Bid created",
                f"""
Your bid of {new_bid.amount} has been added to {item.title}
""",
            )
            return True
        NotificationService.add_notification(
            user,
            "Bid too low",
            f"""
        Your bid of {new_bid.amount} was not the highest for {item.title}
        """,
        )
        return False

    @classmethod
    def check_rebid(cls, user, item_id):
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

    @classmethod
    def get_bid_by_item_id(cls, item_id):
        bid = UserBids.objects.get(item_id_id = item_id)
        print(bid)
        return bid

    @classmethod
    def get_max_bid(cls, item_id):
        try:
            max_bid = UserBids.objects.filter(item_id=item_id).latest("amount")
        except ObjectDoesNotExist:
            return None

        return max_bid

    @classmethod
    def accept_bid(cls, bid: UserBids):
        item = bid.item_id
        item.is_sold = True
        item.save()

        NotificationService.add_notification(
            bid.user_id,
            "Bid accepted",
            f"""
Your bid for {bid.item_id} of {bid.amount} has been accepted by {bid.item_id.seller.username}.
You can finish the checkout process by going to the purchases tab
""",
        )
        bid.status = "ACCEPTED"
        bid.save()

        all_loser_bids = UserBids.objects.filter(~Q(user_id=bid.user_id), item_id=item)
        for loser_bid in all_loser_bids:
            NotificationService.add_notification(
                loser_bid.user_id,
                "Bid rejected",
                f"""
Your bid for {loser_bid.item_id} of {loser_bid.amount} has been rejected by {loser_bid.item_id.seller.username}
""",
            )
            loser_bid.status = "REJECTED"
            loser_bid.save()

    @classmethod
    def get_user_bids(cls, user, active=True):
        """
        get current users bids
        Q negation means filter out any item that matches the criteria
        """

        bids = UserBids.objects.filter(
            ~Q(status="COMPLETED"),
            ~Q(status="REJECTED"),
            user_id=user
        ).order_by("-timestamp")
        return bids

    @classmethod
    def get_bids_for_item(cls, item, status=None):
        if status is None:
            bids = UserBids.objects.filter(
                Q(status="PENDING") | Q(status="ACCEPTED"),
                item_id=item
            )
        else:
            bids = UserBids.objects.filter(
                status=status,
                item_id=item
            )
        return bids


    @classmethod
    def get_all_bids(cls):
        """
        :return: QuerySet of UserBid objects
        """
        bids = UserBids.objects.all()
        return bids

    @classmethod
    def get_bids_for_user_items(cls, user):
        """
        get bids on current users items
        """
        users_items = Item.objects.filter(seller=user)
        bids = UserBids.objects.filter(item_id__in=users_items).order_by("-timestamp")
        return bids

    @staticmethod
    def get_accepted_bids(user):
        pass
