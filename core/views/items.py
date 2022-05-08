from decimal import Decimal
from django.shortcuts import render, redirect
from core.services.category_service import CategoryService
from django.contrib.auth.decorators import login_required
from core.forms.item_form import ItemCreateForm
from core.forms.bid_form import BidCreateForm
from core.services.item_service import ItemService
from core.services.bid_service import BidService


bid_service = BidService()
cat_service = CategoryService()
item_service = ItemService()
ctx = {
    "items": item_service.get_all_items(),
}


def items_page(request):
    return render(request, "../templates/items/items.html", context=ctx)


def item_details(request, item_id):
    ctx["item"] = item_service.get_item_by_id(item_id)
    # TODO: fix late update when bidding
    max_bid = bid_service.get_max_bid(item_id)
    max_bid = max_bid.amount if max_bid is not None else 0
    ctx["bid_form"] = BidCreateForm(
        initial={"amount": max_bid}
    )

    if request.method == "POST":
        form = BidCreateForm(request.POST)
        if form.is_valid():
            result = bid_service.add_bid(form, request.user, ctx["item"])
        if result:
            # TODO: Some green bar or somethigng to validate users feelings
            pass

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
