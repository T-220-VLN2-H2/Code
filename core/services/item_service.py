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

    def delete_item(self):
        print("Do something")
        # TODO

    def update_item(self):
        print("Do something")
        # TODO

    @staticmethod
    def get_all_items():
        items = Item.objects.all()
        return items


    def get_active_sales(self, user):
        active_sales = Item.objects.filter()

    def get_all_images(self):
        print("Do something")
        # TODO

    def sort_items(self):
        print("Do something")
        # TODO
