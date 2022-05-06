from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from models.user_ratings import UserRatings


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = [
            "id",
            "last_login",
            "is_superuser",
            "groups",
            "user_permissions",
            "is_staff",
            "is_active",
            "date_joined",
        ]
        widgets = {
            "username": widgets.TextInput(attrs={"class": "form-control"}),
            "first_name": widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control"}),
            "email": widgets.TextInput(
                attrs={"class": "form-control", "type": "email"}
            ),
            "password": widgets.TextInput(
                attrs={"class": "form-control", "type": "password"}
            ),
        }

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ["id", "user_name", "email", "password"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "bio": widgets.TextInput(attrs={"class": "form-control"}),
        }


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": widgets.TextInput(attrs={"class": "form-control"}),
            "password": widgets.TextInput(
                attrs={"class": "form-control", "type": "password"}
            ),
        }

class UserRatingForm(ModelForm):
    class Meta:
        model = UserRatings
        field = ["Rating"]
        widgets = {
            "Rating": widgets.NumberInput(attrs={'class': 'Stars'})
        }
