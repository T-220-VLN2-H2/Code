from django.shortcuts import render
from .data import items, user
from core.services.category_service import CategoryService

cat_service = CategoryService()
ctx = {
    "categories": cat_service.get_all_category_items(),
    "sub_categories": cat_service.categories_with_parents(),
}


def home(request):
    ctx["user"] = request.user
    return render(request, "../templates/categories/home.html", context=ctx)


def category_page(request, cat_id):
    ctx["user"] = request.user
    for cat in ctx['categories']:
        if cat.id == int(cat_id):
            ctx["selected_category"] = cat
            ctx["category_items"] = [
                item for item in items if item["category"] == cat.id
            ]
            if cat.id in ctx['sub_categories']:
                for sub_cat in ctx['sub_categories'][cat.id]:
                    ctx["category_items"] += [
                        item for item in items if item["category"] == sub_cat.id
                    ]
    return render(request, "../templates/categories/category_page.html", context=ctx)
