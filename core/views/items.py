from django.shortcuts import render
from .data import categories, items, categories_with_parents


def items_page(request):
    ctx = {
        "categories": categories,
        "items": items,
        "sub_categories": categories_with_parents,
    }
    print(ctx)
    return render(request, "../templates/items/items.html", context=ctx)


def item_details(request, item_id):
    ctx = {"categories": categories, "sub_categories": categories_with_parents}
    for item in items:
        if item["id"] == int(item_id):
            ctx["item"] = item
    return render(request, "../templates/items/item_details.html", context=ctx)
