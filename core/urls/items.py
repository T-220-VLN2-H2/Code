from django.urls import path

from ..views import items

urlpatterns = [
    path("items", items.items_page, name="items"),
    path("items/create/", items.item_create, name="item_create"),
    path("items/<item_id>/", items.item_details, name="item_details"),
]
