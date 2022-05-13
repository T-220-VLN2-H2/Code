from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from core.models import Profile


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
        fields = ["first_name", "last_name"]
        # exclude = ["id", "user_name", "email", "password"]
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["description"]
        widgets = {
            "description": widgets.Textarea(
                attrs={"class": "form-control", "rows": "8"}
            ),
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
