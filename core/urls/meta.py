from django.urls import path

from ..views import meta, search

urlpatterns = [
    path("", meta.home, name="index_page"),
    path("login", meta.login_page, name="login_page"),
    path("register", meta.register, name="register_page"),
    path("search", search.search_result, name="search")
]
