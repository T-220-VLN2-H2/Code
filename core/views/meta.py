from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from core.forms.user_form import UserLoginForm
from core.services.item_service import ItemService


def home(request):
    folder_path = "../templates/"
    ctx = {
        "recent_items": ItemService.get_recently_added_items(),
        "user": request.user,
    }
    return render(request, f"{folder_path}/index.html", context=ctx)


def register(request):
    folder_path = "../templates/"
    ctx = {"user": request.user}
    if request.user.is_authenticated:
        return redirect("user_home")
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()  # load the profile instance created by the signal
            new_user.profile.birth_date = form.cleaned_data.get("birth_date")
            new_user.save()
            raw_password = form.cleaned_data.get("password1")
            new_user = authenticate(username=new_user.username, password=raw_password)
            ctx["user"] = new_user
            login(request, new_user)
            return redirect("user_home")
        ctx["form"] = form
    else:
        ctx["form"] = UserCreationForm
    return render(request, f"{folder_path}/register.html", context=ctx)


def login_page(request):
    folder_path = "../templates/"
    ctx = {"user": request.user}
    if request.user:
        ctx["user"] = request.user
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            print("valid")
    else:
        ctx["form"] = UserLoginForm()

    return render(request, f"{folder_path}/login.html", context=ctx)
