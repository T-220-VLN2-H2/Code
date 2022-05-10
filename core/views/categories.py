from django.shortcuts import render
from core.services.category_service import CategoryService
from core.services.item_service import ItemService
from core.services.image_service import ImageService


def home(request):
    item_service = ItemService()
    ctx = {"items": item_service.get_all_items(), "user": request.user}
    return render(request, "../templates/categories/home.html", context=ctx)


def category_page(request, cat_id):
    import re

    image_service = ImageService()
    item_service = ItemService()
    cat_service = CategoryService()
    try:
        sort = request.GET["sort"]
    except:
        sort = "default"
    ctx = {
        "items": item_service.get_all_items(sort=sort),
        "user": request.user,
    }
    categories = cat_service.get_all_category_items()
    sub_categories = cat_service.categories_with_parents()
    # TODO: reduce nesting
    for cat in categories:
        cat_id = re.sub("\D", "", cat_id)  # remove all non-digits
        if cat.id == int(cat_id):
            ctx["selected_category"] = cat
            ctx["category_items"] = [
                (item, image_service.get_images(item))
                for item in ctx["items"]
                if item.category.id == cat.id
            ]
            if cat.id in sub_categories:
                for sub_cat in sub_categories[cat.id]:
                    ctx["category_items"] += [
                        (item, image_service.get_images(item))
                        for item in ctx["items"]
                        if item.category.id == sub_cat.id
                    ]

    return render(request, "../templates/categories/category_page.html", context=ctx)
