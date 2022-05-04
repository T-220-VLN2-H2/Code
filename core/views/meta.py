from django.shortcuts import render
from .data import categories, items, categories_with_parents, user

folder_path = "../templates/"


def home(request):
    ctx = {
        "categories": categories,
        "items": items,
        "sub_categories": categories_with_parents,
        "user": user
    }
    return render(request, f"{folder_path}/index.html", context=ctx)


def register(request):
    if request.method == "POST":
        print("Why are you requesting me???")
    ctx = {
        "categories": categories,
        "sub_categories": categories_with_parents,
        "user": user
    }
    return render(request, f"{folder_path}/register.html", context=ctx)


def login(request):
    if request.method == "POST":
        print("Why are you requesting me???")
    ctx = {
        "categories": categories,
        "sub_categories": categories_with_parents
    }
    return render(request, f"{folder_path}/login.html", context=ctx)
