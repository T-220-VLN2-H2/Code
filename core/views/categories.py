from django.shortcuts import render


def home(request):
    categories = [
        {"id": 1, "name": "Electronics"},
        {"id": 2, "name": "Furniture"}
    ]
    ctx = {
        "categories": categories
    }
    return render(request, '../templates/categories/home.html', context=ctx)
