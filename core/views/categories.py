from django.shortcuts import render
from core.services.category_service import CategoryService
from core.services.item_service import ItemService
from core.services.image_service import ImageService


def home(request):
    ctx = {"user": request.user}
    return render(request, "../templates/categories/home.html", context=ctx)


def category_page(request, cat_id):
    import re

    cat_id = re.sub("\D", "", cat_id)  # remove all non-digits
    try:
        sort = request.GET["sort"]
    except:
        sort = "default"
    ctx = {
        "items": ItemService.get_all_items(sort=sort, category=cat_id),
        "user": request.user,
    }
    return render(request, "../templates/categories/category_page.html", context=ctx)
