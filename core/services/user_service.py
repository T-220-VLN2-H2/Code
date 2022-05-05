from django.shortcuts import redirect, render
from Code.core.forms.user_form import UserCreateForm


class UserService:
    def get_user_info(request):
        if request.method == "GET":
            print("do something")
            # TODO validate the request, find the corresponding user in DB and return object. Else raise error.

    def set_user_info(request):
        if request.method == "PATCH":
            print("do something")
            # TODO validate the request, find the corresponding user in DB and update information. Else raise error.

    def delete_user(request):
        if request.method == "DELETE":
            print(1)
            # TODO validate the request, forward to DB to remove information, return success. Else raise error.

    def create_user(request):
        if request.method == "POST":
            form = UserCreateForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                user_image = UserImage(image=request.POST["image"], user=user)
                user_image.save()
                return redirect("user-index")
        else:
            form = UserCreateForm()
        return render(request, "user/create_user.html", {"form": form})
