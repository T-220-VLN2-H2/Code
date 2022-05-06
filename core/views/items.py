from django.shortcuts import render, redirect
from core.services.category_service import CategoryService
from django.contrib.auth.decorators import login_required
from core.forms.item_form import ItemCreateForm
from core.services.item_service import ItemService


cat_service = CategoryService()
item_service = ItemService()
ctx = {
    "items": item_service.get_all_items(),
}


def items_page(request):
    return render(request, "../templates/items/items.html", context=ctx)


def item_details(request, item_id):
    ctx["item"] = item_service.get_item_by_id(item_id)
    if ctx["item"] is None:
        return redirect("index_page")
    return render(request, "../templates/items/item_details.html", context=ctx)


@login_required
def item_create(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            result = item_service.create_item(form, request.user)
            print(result)
    else:
        ctx["form"] = ItemCreateForm()
    return render(request, "../templates/items/items_create.html", context=ctx)
