from core.models.item import Item
from core.models.user_sales import UserSales
from django.core.exceptions import ObjectDoesNotExist


class ItemService:
    @staticmethod
    def create_item(form, user):
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
        return True

    def create_item(price, condition, category, delivery_option):
        new_item = Item(price, condition, category, delivery_option)
        new_item.save()
        print('Do something')
        #TODO validate that all item information is correct and add to the DB. 

    def delete_item(id):
        print('Do something')
        #TODO remove item from DB 

    def update_item(**kwargs):
        print('Do something')
        #TODO update item in DB

    @staticmethod
    def get_all_items(is_sold=False):
        items = Item.objects.filter(is_sold=is_sold)
        return items

    @staticmethod
    def get_sale_items(user, is_sold=False):
        active_sales = UserSales.objects.get(user_id=user)
        sale_items = active_sales.items.filter(is_sold=is_sold)
        return sale_items

    @staticmethod
    def get_item_by_id(item_id):
        item = Item.objects.get(id=item_id)
        return item

    @staticmethod
    def get_recently_added_items():
        recent_items = Item.objects.all().order_by("-id")[:12]
        return recent_items

    def get_all_images(self):
        print('Do something')
        #TODO get all images with itemID and return

    def sort_items(**kwargs):
        print('Do something')
        #TODO sort items by name or price