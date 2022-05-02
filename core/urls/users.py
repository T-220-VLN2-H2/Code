from django.urls import path

from ..views import users

urlpatterns = [
    path('users', users.home, name='user_home'),
    path('users/<id>', users.profile, name='user_profile'),
    path('users/<id>/edit', users.edit, name='user_edit'),
    path('users/<id>/history', users.history, name='user_history'),
    path('users/<id>/messages', users.messages, name='user_messages'),
]
