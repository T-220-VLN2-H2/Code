from core.models.item import Item
from django.core.exceptions import ObjectDoesNotExist
from core.services.image_service import ImageService

image_service = ImageService()


class ItemService:
    @staticmethod
    def create_item(form, user):
        new_item = form.save(commit=False)
        new_item.seller = user
        new_item.save()
        return True

    @staticmethod
    def get_all_items(is_sold=False):
        items = Item.objects.filter(is_sold=is_sold)
        return items

    @staticmethod
    def get_sale_items(user, is_sold=False):
        items = Item.objects.filter(seller=user, is_sold=is_sold)
        return items

    @staticmethod
    def get_item_by_id(item_id):
        item = Item.objects.get(id=item_id)
        return item

    @staticmethod
    def get_recently_added_items():
        recent_items = Item.objects.all().order_by("-id")[:12]
        return recent_items
