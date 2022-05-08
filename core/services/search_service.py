from core.models.item import Item


class SearchService:
    @staticmethod
    def item_search(q=None):
        if q is None:
            return Item.objects.all().values()
        return Item.objects.filter(title__icontains=q)

    def category_search(request):
        print("Do something")
        # TODO idea 1: get all items that have this category id and return them. Return empty list if no items belong to the category.
