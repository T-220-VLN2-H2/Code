from django.forms import ModelForm, widgets
from core.models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ["id"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "user_name": widgets.TextInput(attrs={"class": "form-control"}),
            "email": widgets.TextInput(attrs={"class": "form-control"}),
            "bio": widgets.TextInput(attrs={"class": "form-control"}),
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ["id"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "bio": widgets.TextInput(attrs={"class": "form-control"}),
        }
