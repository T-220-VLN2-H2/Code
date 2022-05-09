from django.shortcuts import redirect
from core.models import Profile, UserRatings
from django.db.models import Avg


class UserService:
    def get_user_info(self, user_id):
        user = Profile.objects.get(id=user_id)
        return user

    def set_user_info(self, user, first_name=None, last_name=None, bio=None):
        pass
        # probably won't need this

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
