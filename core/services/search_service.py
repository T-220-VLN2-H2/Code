from core.models.item import Item
from core.services.image_service import ImageService
from core.services.item_service import ItemService


class SearchService:
    @classmethod
    def item_search(cls, q=None, sort="default"):
        if q is None:
            items = Item.objects.filter(is_sold=False).values()
            return items
        else:
            items = (
                Item.objects.filter(title__icontains=q)
                .filter(is_sold=False)
                .order_by(ItemService.get_sort(sort))
            )
        result = [(item, ImageService.get_images(item)) for item in items]
        return result

    @classmethod
    def category_search(cls, category_id):
        print("Do something")
        # TODO idea 1: get all items that have this category id and return them. Return empty list if no items belong to the category.
