from django.shortcuts import render, redirect
from core.services.category_service import CategoryService
from django.contrib.auth.decorators import login_required
from core.forms.item_form import ItemCreateForm
from core.forms.bid_form import BidCreateForm
from core.services.item_service import ItemService
from core.services.bid_service import BidService
from core.services.image_service import ImageService
from core.services.user_service import UserService


class ContextServices:
    bid_service = BidService()
    cat_service = CategoryService()
    item_service = ItemService()
    image_service = ImageService()
    user_service = UserService()

    ctx = {
        "items": item_service.get_all_items(),
    }


def items_page(request):
    services = ContextServices()
    return render(request, "../templates/items/items.html", context=services.ctx)


def item_details(request, item_id):
    services = ContextServices()
    item = services.item_service.get_item_by_id(item_id)
    services.ctx["item"] = item
    # TODO: fix late update when bidding
    max_bid = services.bid_service.get_max_bid(item_id)
    max_bid = max_bid.amount if max_bid is not None else 0
    services.ctx["images"] = services.image_service.get_images(services.ctx["item"])
    services.ctx["similar_items"] = services.item_service.get_similar_items(
        services.ctx["item"]
    )
    services.ctx["seller_avg_rating"] = services.user_service.get_user_rating(item.seller.id)['rating__avg']
    print(item.seller.profile.image)
    if request.method == "POST":
        form = BidCreateForm(request.POST)
        result = None
        if form.is_valid():
            result = services.bid_service.add_bid(
                form, request.user, services.ctx["item"]
            )
        if result:
            # TODO: Some green bar or somethigng to validate users feelings
            max_bid = services.bid_service.get_max_bid(item_id).amount

    if services.ctx["item"] is None:
        return redirect("index_page")

    services.ctx["bid_form"] = BidCreateForm(initial={"amount": max_bid})
    return render(request, "../templates/items/item_details.html", context=services.ctx)


@login_required
def item_create(request):
    services = ContextServices()
    if request.method == "POST":
        image_service = ImageService()
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            item = services.item_service.create_item(form, request.user)
            image_service.create_image(request.FILES.getlist("images"), item)

    else:
        services.ctx["form"] = ItemCreateForm()
    return render(request, "../templates/items/items_create.html", context=services.ctx)
