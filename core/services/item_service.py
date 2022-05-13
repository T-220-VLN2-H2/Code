from core.models import Item, Image
from core.services.image_service import ImageService
from core.services.bid_service import BidService
from django.core.exceptions import ObjectDoesNotExist


class ItemService:
    @classmethod
    def get_sort(cls, x):
        sort = {
            "default": "price",
            "price_hi": "-price",
            "price_lo": "price",
            "name": "title",
        }
        if x not in sort:
            x = "default"
        return sort[x]

    @classmethod
    def create_item(cls, form, user):
        new_item = form.save(commit=False)
        new_item.seller = user

        new_item.save()

        if new_item.images.count() == 0:
            new_item.images.add(Image.objects.get(id=385))

        return new_item

    @classmethod
    def delete_item(cls, id):
        print("Do something")
        # TODO remove item from DB

    @classmethod
    def update_item(cls, **kwargs):
        print("Do something")
        # TODO update item in DB

    @classmethod
    def get_all_items(cls, is_sold=False, category=None, sort="default"):
        if category is not None:
            items = Item.objects.filter(is_sold=is_sold, category=category).order_by(
                cls.get_sort(sort)
            )
        else:
            items = Item.objects.filter(is_sold=is_sold).order_by(cls.get_sort(sort))
        return items

    @classmethod
    def get_user_items_with_bids(cls, user):
        items = Item.objects.filter(seller=user)
        items_with_bids = [(item, BidService.get_bids_for_item(item)) for item in items]
        return items_with_bids

    @classmethod
    def get_sold_items(cls, user):
        items = Item.objects.filter(seller=user, is_sold=True)
        items = [
            (item, BidService.get_bids_for_item(item, "COMPLETED")) for item in items
        ]
        return items

    @classmethod
    def get_sale_items(cls, user):
        items = Item.objects.filter(seller=user)
        return items

    @classmethod
    def get_item_by_id(cls, item_id):
        item = Item.objects.get(id=item_id)
        return item

    @classmethod
    def get_recently_added_items(cls):
        recent_items = Item.objects.filter(is_sold=False).order_by("-id")[:12]
        recent_item = [(item, ImageService.get_images(item)) for item in recent_items]
        return recent_item

    @classmethod
    def get_similar_items(cls, current_item):
        similar_items = Item.objects.filter(
            category=current_item.category, is_sold=False
        )[:4]
        similar_items = [
            (item, ImageService.get_images(item))
            for item in similar_items
            if item != current_item
        ]
        return similar_items

    @classmethod
    def get_items_offset(cls, category=None, sort="default", offset=0, count=12):
        items = Item.objects.filter(is_sold=False, category=category).order_by(cls.get_sort(sort))[offset:][:count]
        return items

    @classmethod
    def get_all_items_count(cls, category=None):
        items_count = Item.objects.filter(category=category).count()
        return items_count
