from django.urls import path

from ..views import meta

urlpatterns = [
    path("", meta.home, name="index_page"),

]
