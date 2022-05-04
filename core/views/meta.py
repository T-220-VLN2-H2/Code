from django.shortcuts import render
from .data import categories, items, categories_with_parents

folder_path = "../templates/"


def home(request):
    return render(request, f"{folder_path}/index.html")
