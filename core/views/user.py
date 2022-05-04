from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .data import (
    categories,
    user,
    categories_with_parents,
    items,
    ratings,
    user_messages,
)

folder_path = "../templates/user"


ctx = {
    "categories": categories,
    "sub_categories": categories_with_parents,
    "ratings": ratings,
    "items": items,
    "user_messages": user_messages,
}


@login_required
def home(request):
    if request.user is None:
        return redirect("/login")
    else:
        ctx["user"] = request.user
    return render(request, f"{folder_path}/index.html", context=ctx)


@login_required
def edit(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/edit.html", context=ctx)


@login_required
def profile(request, id):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/user.html", context=ctx)


@login_required
def history(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/history.html", context=ctx)


@login_required
def messages(request):
    ctx["user"] = request.user
    return render(request, f"{folder_path}/messages.html", context=ctx)
