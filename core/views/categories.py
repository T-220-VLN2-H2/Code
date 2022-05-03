from django.shortcuts import render

categories = [
        {"id": 1, "name": "Electronics"},
        {"id": 2, "name": "Furniture"}
    ]


def home(request):
    ctx = {
        "categories": categories
    }
    return render(request, '../templates/categories/home.html', context=ctx)


def category_page(request, id):
    ctx = {
        "categories": categories
    }
    for cat in categories:
        if cat['id'] == int(id):
            ctx["selected_category"] = cat
            ctx["category_items"] = [{"id": 1, "name": cat['name']+" item"}]
            print(ctx)

    return render(request, '../templates/categories/category_page.html', context=ctx)

