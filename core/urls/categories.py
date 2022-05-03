from django.urls import path

from ..views import categories

urlpatterns = [
    path('category', categories.home, name='category_home'),
    path('category/<cat_id>', categories.category_page, name="category_page")
]
