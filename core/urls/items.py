from django.urls import path

from ..views import items

urlpatterns = [
    path("items", items.items_page, name="items"),
    path("items/<item_id>", items.item_details, name="item_details"),
]
