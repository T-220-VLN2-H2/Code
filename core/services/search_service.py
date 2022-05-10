from core.models.item import Item
from core.services.image_service import ImageService


class SearchService:
    @classmethod
    def item_search(cls, q=None):
        if q is None:
            items = Item.objects.filter(is_sold=False).values()
            return items
        else:
            items = Item.objects.filter(title__icontains=q).filter(is_sold=False)
        result = [(item, ImageService.get_images(item)) for item in items]
        return result

    @classmethod
    def category_search(cls, category_id):
        print("Do something")
        # TODO idea 1: get all items that have this category id and return them. Return empty list if no items belong to the category.
