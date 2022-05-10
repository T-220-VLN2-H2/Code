from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.services.category_service import CategoryService
from core.services.notification_service import NotificationService
from core.services.item_service import ItemService
from core.services.bid_service import BidService
from core.services.user_service import UserService
from core.services.image_service import ImageService
from core.forms.user_form import UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class ContextServices:
    user_service = UserService()
    cat_service = CategoryService()
    item_service = ItemService()
    bid_service = BidService()
    notification_service = NotificationService()
    image_service = ImageService()
    folder_path = "../templates/user"

    ctx = {
        "items": item_service.get_all_items(),
    }


@login_required
def home(request):
    services = ContextServices()
    services.ctx["user"] = request.user
    services.ctx["ratings"] = services.user_service.get_user_ratings(request.user)
    # TODO: implement count for get_sale_items
    services.ctx["items"] = services.item_service.get_sale_items(request.user.id)[:7]
    return render(request, f"{services.folder_path}/index.html", context=services.ctx)


@login_required
def edit(request):
    services = ContextServices()
    services.ctx["user"] = request.user
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        services.image_service.update_profile_image(
            request.user, request.FILES["images"]
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return HttpResponseRedirect(reverse("user_home"))
    else:
        services.ctx["user_form"] = UserUpdateForm(
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )
        services.ctx["profile_form"] = ProfileUpdateForm(
            initial={"description": request.user.profile.description}
        )
    return render(request, f"{services.folder_path}/edit.html", context=services.ctx)


@login_required
def profile(request, id):
    import re
    id = re.sub('\D', '', id)  # removes all non digits
    services = ContextServices()

    if int(id) == request.user.id:
        return redirect("user_home")

    target_user = services.user_service.get_user_info(id)
    services.ctx["ratings"] = services.user_service.get_user_ratings(target_user)
    services.ctx["items"] = services.item_service.get_sale_items(target_user.id)[:7]
    services.ctx["target_user"] = target_user
    services.ctx["user"] = request.user

    return render(request, f"{services.folder_path}/user.html", context=services.ctx)


@login_required
def history(request):
    services = ContextServices()
    services.ctx["user"] = request.user
    services.ctx["active_sales"] = services.item_service.get_sale_items(request.user)
    services.ctx["sold_items"] = services.item_service.get_sale_items(
        request.user, is_sold=True
    )
    services.ctx["bids"] = services.bid_service.get_user_bids(request.user)
    return render(request, f"{services.folder_path}/history.html", context=services.ctx)


@login_required
def messages(request):
    services = ContextServices()
    services.ctx["user"] = request.user
    services.ctx["user_messages"] = services.notification_service.get_notifications(
        request.user
    )
    return render(
        request, f"{services.folder_path}/messages.html", context=services.ctx
    )


@login_required
def item_bids(request):
    services = ContextServices()
    services.ctx["item_bids"] = services.bid_service.get_bids_for_user_items(
        request.user
    )
    return render(request, f"{services.folder_path}/history.html", context=services.ctx)
