from core.models.item import Item
from django.core.exceptions import ObjectDoesNotExist
from core.services.image_service import ImageService

image_service = ImageService()


class ItemService:
    @staticmethod
    def create_item(form, user):
<<<<<<< HEAD
        form.save()
        item = Item.objects.last()
        try:
            user_sale = UserSales.objects.get(user_id=user)
        except ObjectDoesNotExist:
            user_sale = UserSales()
            user_sale.user_id = user
            user_sale.save()
        user_sale.items.add(item)
        user_sale.save()
<<<<<<< HEAD
=======
        new_item = form.save(commit=False)
        new_item.seller = user
        new_item.save()
>>>>>>> f8d41ed441c8bea72d43079b8e7435713cb65aef
        return True
=======
        return item

    def delete_item(id):
        print("Do something")
        # TODO remove item from DB

    def update_item(**kwargs):
        print("Do something")
        # TODO update item in DB
>>>>>>> origin/main

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
<<<<<<< HEAD
        return recent_items
=======
        recent_item = [(item, image_service.get_images(item)) for item in recent_items]
        return recent_item

    def get_similar_items(self, item):
        similar_items = Item.objects.filter(category=item.category)[:4]
        similar_items = [
            (item, image_service.get_images(item)) for item in similar_items
        ]
        return similar_items

    def sort_items(**kwargs):
        print("Do something")
        # TODO sort items by name or price
>>>>>>> origin/main
