from django.shortcuts import render
from .data import categories, items, categories_with_parents


def home(request):
    ctx = {
        "categories": categories,
        "sub_categories": categories_with_parents
    }
    return render(request, '../templates/categories/home.html', context=ctx)


def category_page(request, cat_id):

    ctx = {
        "categories": categories,
        "sub_categories": categories_with_parents
    }

    for cat in categories:
        if cat['id'] == int(cat_id):
            ctx["selected_category"] = cat
            ctx["category_items"] = [item for item in items if item['category'] == cat['id']]
            if cat['id'] in categories_with_parents:
                for sub_cat in categories_with_parents[cat['id']]:
                    ctx["category_items"] += [item for item in items if item['category'] == sub_cat['id']]
    return render(request, '../templates/categories/category_page.html', context=ctx)

