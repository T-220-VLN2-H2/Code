from core.forms.user_form import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from core.services.bid_service import BidService
from core.services.category_service import CategoryService
from core.services.image_service import ImageService
from core.services.item_service import ItemService
from core.services.notification_service import NotificationService
from core.services.order_service import OrderService
from core.services.user_service import UserService
from datetime import datetime

from core.models import UserBids

folder_path = "../templates/user"
ctx = {}


def add_information(bids: UserBids):
    """Adds time and highest bid information for recents template"""

    now = datetime.now()

    for bid in bids:
        item = bid.item_id
        # add max bid
        max_bid = bid
        max_bid = max_bid.amount if max_bid is not None else 0
        item.max_bid = max_bid
        # add days/hours since created
        then = item.date_created
        time_since = now - then.replace(tzinfo=None)
        item.time_since_hours = int(time_since.seconds / 60 / 60 % 24)
        item.time_since_days = time_since.days
        # add single image
        # image = item.images.first()
        # item.image = image


@login_required
def home(request):
    ctx["user"] = request.user
    ctx["ratings"] = UserService.get_user_ratings(request.user)
    bids = BidService.get_max_bids()
    add_information(bids)
    ctx["items"] = [itm.item_id for itm in bids]
    ctx["items"] += ItemService.get_sale_items(request.user)

    avg_rating = UserService.get_user_rating(request.user.id)["rating__avg"]

    if avg_rating and avg_rating.is_integer():
        avg_rating = int(avg_rating)

    ctx["avg_rating"] = avg_rating
    return render(request, f"{folder_path}/index.html", context=ctx)


@login_required
def edit(request):
    ctx["user"] = request.user
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if "images" in request.FILES:
            ImageService.update_profile_image(request.user, request.FILES["images"])
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return redirect("user_home")
    else:
        ctx["user_form"] = UserUpdateForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )
        ctx["profile_form"] = ProfileUpdateForm(
            initial={"description": request.user.profile.description}
        )
    return render(request, f"{folder_path}/edit.html", context=ctx)


@login_required
def profile(request, id):
    import re

    id = re.sub("\D", "", id)  # removes all non digits

    if int(id) == request.user.id:
        return redirect("user_home")

    target_user = UserService.get_user_info(id)
    ctx["ratings"] = UserService.get_user_ratings(target_user)
    ctx["items"] = ItemService.get_sale_items(target_user.id)

    add_information(ctx["items"])

    ctx["target_user"] = target_user
    ctx["user"] = request.user
    avg_rating = UserService.get_user_rating(target_user.id)["rating__avg"]

    if avg_rating and avg_rating.is_integer():
        avg_rating = int(avg_rating)

    ctx["avg_rating"] = avg_rating

    return render(request, f"{folder_path}/user.html", context=ctx)


@login_required
def history(request):
    ctx["user"] = request.user
    # Active listings is a tuple of items and bids for that item
    ctx["active_listings"] = ItemService.get_user_items_with_bids(request.user)
    ctx["bids"] = BidService.get_user_bids(request.user, False)

    ctx["sold_items"] = ItemService.get_sold_items(request.user)
    ctx["purchases"] = OrderService.get_orders(request.user)
    if request.method == "POST":
        order_id = request.POST.getlist("order_id")
        bid_id = request.POST.getlist("bid")
        if order_id:
            order_id = request.POST["order_id"]
            rating = request.POST["rating"]
            order = OrderService.get_order_details(order_id)
            order.rating = rating
            order.save()
            return redirect(reverse("user_history") + "#purchases")
        if bid_id:
            accepted_bid_id = request.POST["bid"]
            accepted_bid = BidService.get_bid_by_id(int(accepted_bid_id))
            BidService.accept_bid(accepted_bid)

    return render(request, f"{folder_path}/history.html", context=ctx)


@login_required
def messages(request):
    ctx["user"] = request.user
    ctx["user_messages"] = NotificationService.get_notifications(request.user)
    for message in ctx["user_messages"]:
        NotificationService.mark_notification_read(message)
    return render(request, f"{folder_path}/messages.html", context=ctx)


@login_required
def item_bids(request):
    ctx["item_bids"] = BidService.get_bids_for_user_items(request.user)
    return render(request, f"{folder_path}/history.html", context=ctx)
