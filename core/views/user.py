from django.shortcuts import render
from .data import categories, user

folder_path = "../templates/user"


def home(request):
    ctx = {"categories": categories}

    return render(request, f"{folder_path}/index.html", context=ctx)


def edit(request):

    return render(request, f"{folder_path}/edit.html")


def profile(request, id):
    ctx = {"user": user}
    return render(request, f"{folder_path}/user.html", context=ctx)


def history(request, id):
    ctx = {"categories": categories}

    return render(request, f"{folder_path}/history.html", context=ctx)


def messages(request, id):
    return render(request, f"{folder_path}/messages.html")
