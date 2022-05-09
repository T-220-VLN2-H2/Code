from django.urls import path
from ..views import user
from ..views import meta, search

urlpatterns = [
    path("", meta.home, name="index_page"),
    path("login", meta.login_page, name="login_page"),
    path("register", meta.register, name="register_page"),
    path("search", search.search_result, name="search"),
    path("user/history#active-sales", user.history, name="active_sales"),
    path("user/history#bids", user.history, name="bids"),
]
