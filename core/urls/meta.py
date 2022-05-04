from django.urls import path

from ..views import meta

urlpatterns = [
    path("", meta.home, name="index_page"),
    path("login", meta.login, name="login_page"),
    path("register", meta.register, name="register_page"),
]
