from django.shortcuts import render
from core.services.category_service import CategoryService
from core.services.item_service import ItemService
from core.services.image_service import ImageService


def home(request):
    ctx = {"user": request.user}
    return render(request, "../templates/categories/home.html", context=ctx)


def category_page(request, cat_id):
    import re
    item_count = ItemService.get_all_items_count(category=cat_id)
    max_page = int(item_count / 12)
    try:
        page = request.GET['page']
        offset = ((int(page)) * 10)
        if int(page) == 1 or int(page) < 1:
            page = 1
            offset = 0
    except:
        page = 1
        offset = 0

    cat_id = re.sub("\D", "", cat_id)  # remove all non-digits
    try:
        sort = request.GET["sort"]
    except:
        sort = "default"
    ctx = {
        "items": ItemService.get_items_offset(category=cat_id, sort=sort, offset=offset),
        "user": request.user,
        "page": page,
        "max_page": max_page
    }
    return render(request, "../templates/categories/category_page.html", context=ctx)
