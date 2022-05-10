from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.services.category_service import CategoryService
from core.services.notification_service import NotificationService
from core.services.item_service import ItemService
from core.services.bid_service import BidService
from core.services.user_service import UserService
from core.forms.user_form import UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from .data import (
    user,
    ratings,
    user_messages,
)

user_service = UserService()
cat_service = CategoryService()
item_service = ItemService()
bid_service = BidService()
notification_service = NotificationService()
folder_path = "../templates/user"


ctx = {
    "items": item_service.get_all_items(),
}


@login_required
def home(request):
    ctx["user"] = request.user
    ctx["ratings"] = user_service.get_user_ratings(request.user)
    # TODO: implement count for get_sale_items
    ctx["items"] = item_service.get_sale_items(request.user.id)[:7]
    return render(request, f"{folder_path}/index.html", context=ctx)


@login_required
def edit(request):
    ctx["user"] = request.user
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
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
    # TODO validate id as an int
    if int(id) == request.user.id:
        return redirect("user_home")

    target_user = user_service.get_user_info(id)
    ctx["ratings"] = user_service.get_user_ratings(target_user)
    print(ctx["ratings"])
    ctx["items"] = item_service.get_sale_items(target_user.id)[:7]
    ctx["target_user"] = target_user
    ctx["user"] = request.user

    return render(request, f"{folder_path}/user.html", context=ctx)


@login_required
def history(request):
    ctx["user"] = request.user
    ctx["active_sales"] = item_service.get_sale_items(request.user)
    ctx["sold_items"] = item_service.get_sale_items(request.user, is_sold=True)
    ctx["bids"] = bid_service.get_user_bids(request.user)
    return render(request, f"{folder_path}/history.html", context=ctx)


@login_required
def messages(request):
    ctx["user"] = request.user
    ctx["user_messages"] = notification_service.get_notifications(request.user)
    return render(request, f"{folder_path}/messages.html", context=ctx)


@login_required
def item_bids(request):
    ctx["item_bids"] = bid_service.get_bids_for_user_items(request.user)
    return render(request, f"{folder_path}/history.html", context=ctx)
