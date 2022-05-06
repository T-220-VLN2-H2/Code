from django.shortcuts import render
from core.services.category_service import CategoryService
from core.services.item_service import ItemService

cat_service = CategoryService()
item_service = ItemService()
ctx = {
    "items": item_service.get_all_items(),
}


def home(request):
    ctx["user"] = request.user
    return render(request, "../templates/categories/home.html", context=ctx)


def category_page(request, cat_id):
    ctx["user"] = request.user
    categories = cat_service.get_all_category_items()
    sub_categories = cat_service.categories_with_parents()
    for cat in categories:
        if cat.id == int(cat_id):
            ctx["selected_category"] = cat
            ctx["category_items"] = [
                item for item in ctx["items"] if item.category.id == cat.id
            ]
            if cat.id in sub_categories:
                for sub_cat in sub_categories[cat.id]:
                    ctx["category_items"] += [
                        item for item in ctx["items"] if item.category.id == sub_cat.id
                    ]
    return render(request, "../templates/categories/category_page.html", context=ctx)
