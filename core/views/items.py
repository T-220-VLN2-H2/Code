from core.forms.bid_form import BidCreateForm
from core.forms.item_form import ItemCreateForm
from core.services.bid_service import BidService
from core.services.category_service import CategoryService
from core.services.image_service import ImageService
from core.services.item_service import ItemService
from core.services.user_service import UserService
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


ctx = {}


def items_page(request):
    return render(request, "../templates/items/items.html", context=ctx)


def item_details(request, item_id):
    item = ItemService.get_item_by_id(item_id)
    ctx["item"] = item
    # TODO: fix late update when bidding
    max_bid = BidService.get_max_bid(item_id)
    max_bid = max_bid.amount if max_bid is not None else 0
    ctx["seller_avg_rating"] = UserService.get_user_rating(item.seller.id)[
        "rating__avg"
    ]
    ctx["images"] = ImageService.get_images(ctx["item"])
    ctx["similar_items"] = ItemService.get_similar_items(ctx["item"])
    if request.method == "POST":
        if request.user.is_authenticated:
            form = BidCreateForm(request.POST)
            result = None
            if form.is_valid():
                result = BidService.add_bid(form, request.user, ctx["item"])
            if result:
                # TODO: Some green bar or somethigng to validate users feelings
                max_bid = BidService.get_max_bid(item_id).amount
        else:
            return redirect("user_home")

        if ctx["item"] is None:
            return redirect("index_page")

    ctx["bid_form"] = BidCreateForm(initial={"amount": max_bid})
    ctx['max_bid'] = max_bid
    return render(request, "../templates/items/item_details.html", context=ctx)


@login_required
def item_create(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            item = ItemService.create_item(form, request.user)
            ImageService.create_image(request.FILES.getlist("images"), item)

    else:
        ctx["form"] = ItemCreateForm()
    return render(request, "../templates/items/items_create.html", context=ctx)
