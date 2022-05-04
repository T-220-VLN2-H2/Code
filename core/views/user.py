from django.shortcuts import render
from .data import categories, user, categories_with_parents

folder_path = "../templates/user"


ctx = {
    "categories": categories,
    "user": user,
    "sub_categories": categories_with_parents,
}


def home(request):
    return render(request, f"{folder_path}/index.html", context=ctx)


def edit(request):

    return render(request, f"{folder_path}/edit.html")


def profile(request, id):
    return render(request, f"{folder_path}/user.html", context=ctx)


def history(request):
    return render(request, f"{folder_path}/history.html")


def messages(request):
    return render(request, f"{folder_path}/messages.html")


def messages(request):
    return render(request, f"{folder_path}/messages.html")
