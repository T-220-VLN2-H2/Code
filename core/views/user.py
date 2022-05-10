from core.forms.user_form import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from core.services.bid_service import BidService
from core.services.category_service import CategoryService
from core.services.image_service import ImageService
from core.services.item_service import ItemService
from core.services.notification_service import NotificationService
from core.services.user_service import UserService

folder_path = "../templates/user"
ctx = {}


@login_required
def home(request):
    ctx["user"] = request.user
    ctx["ratings"] = UserService.get_user_ratings(request.user)
    # TODO: implement count for get_sale_items
    ctx["items"] = ItemService.get_sale_items(request.user.id)[:7]
    return render(request, f"{folder_path}/index.html", context=ctx)


@login_required
def edit(request):
    ctx["user"] = request.user
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        ImageService.update_profile_image(request.user, request.FILES["images"])
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return HttpResponseRedirect(reverse("user_home"))
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
    ctx["items"] = ItemService.get_sale_items(target_user.id)[:7]
    ctx["target_user"] = target_user
    ctx["user"] = request.user

    return render(request, f"{folder_path}/user.html", context=ctx)


@login_required
def history(request):
    if request.POST:
        if request.POST["bid"]:
            accepted_bid_id = request.POST["bid"]
            accepted_bid = BidService.get_bid_by_id(int(accepted_bid_id))
            BidService.accept_bid(accepted_bid)

    ctx["user"] = request.user
    ctx["active_sales"] = ItemService.get_sale_items(request.user)
    ctx["sold_items"] = ItemService.get_sale_items(request.user, is_sold=True)
    ctx["bids"] = BidService.get_user_bids(request.user)
    ctx["accepted_bid"] = BidService.get_accepted_bids(request.user)
    ctx["user_item_bids"] = BidService.get_bids_for_user_items(request.user)
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
