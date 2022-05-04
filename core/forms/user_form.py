from django.forms import ModelForm, widgets
from core.models.user import User, Profile


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
            "date_joined"]
        widgets = {
            "username": widgets.TextInput(attrs={"class": "form-control"}),
            "first_name": widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control"}),
            "email": widgets.TextInput(attrs={"class": "form-control", "type": "email"}),
            "password": widgets.TextInput(attrs={"class": "form-control", "type": "password"}),
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
        exclude = ["id", "email", "name", "bio"]
        widgets = {
            "username": widgets.TextInput(attrs={"class": "form-control"}),
            "password": widgets.TextInput(attrs={"class": "form-control"}),
        }
