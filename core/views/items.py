from django.shortcuts import render
from .data import items
from core.services.category_service import CategoryService

cat_service = CategoryService()
ctx = {
    "categories": cat_service.get_all_category_items(),
    "sub_categories": cat_service.categories_with_parents(),
}


def items_page(request):
    ctx["items"] = items
    return render(request, "../templates/items/items.html", context=ctx)


def item_details(request, item_id):
    for item in items:
        if item["id"] == int(item_id):
            ctx["item"] = item
    return render(request, "../templates/items/item_details.html", context=ctx)
