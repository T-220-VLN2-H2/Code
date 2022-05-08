from core.models.item import Item


class SearchService:
    @staticmethod
    def item_search():
        return Item.objects.filter().values()

    def category_search(category_id):
        print("Do something")
        # TODO idea 1: get all items that have this category id and return them. Return empty list if no items belong to the category.
