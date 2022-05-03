from django.db import models
from django.shortcuts import render
from Code.core.forms.user_form import UserCreateForm

def create_user(request):
    if request.method == 'POST':
        print(1)
    else:
        form = UserCreateForm()
    return render(request, 'user/create_user.html',  {
        'form': form
    })

class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'