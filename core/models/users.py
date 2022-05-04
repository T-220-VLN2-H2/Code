from django.db import models
from django.shortcuts import render
from Code.core.forms.user_form import UserCreateForm

class User(models.Model):
    id = models.BigAutoField()
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'

class SearchHistory(models.Model):
    search_string = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

class Notifications(models.Model):
    id = models.BigAutoField()
    message = models.CharField(max_length=255)
