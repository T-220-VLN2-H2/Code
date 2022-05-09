from decimal import Decimal
from django.shortcuts import render, redirect
from core.services.category_service import CategoryService
from django.contrib.auth.decorators import login_required
from core.forms.item_form import ItemCreateForm
from core.forms.bid_form import BidCreateForm
from core.services.item_service import ItemService
from core.services.bid_service import BidService
from core.services.image_service import ImageService
from django.core.files.storage import FileSystemStorage

bid_service = BidService()
cat_service = CategoryService()
item_service = ItemService()
image_service = ImageService()

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
    ctx["images"] = image_service.get_images(ctx["item"])
    if request.method == "POST":
        form = BidCreateForm(request.POST)
        if form.is_valid():
            result = bid_service.add_bid(form, request.user, ctx["item"])
        if result:
            # TODO: Some green bar or somethigng to validate users feelings
            max_bid = bid_service.get_max_bid(item_id).amount

    if ctx["item"] is None:
        return redirect("index_page")

    ctx["bid_form"] = BidCreateForm(initial={"amount": max_bid})
    return render(request, "../templates/items/item_details.html", context=ctx)


@login_required
def item_create(request):
    if request.method == "POST":
        image_service = ImageService()
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            item = item_service.create_item(form, request.user)
            image_service.create_image(request.FILES.getlist('images'), item)

    else:
        ctx["form"] = ItemCreateForm()
    return render(request, "../templates/items/items_create.html", context=ctx)
