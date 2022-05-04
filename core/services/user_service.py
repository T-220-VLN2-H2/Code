from django.shortcuts import redirect, render
from Code.core.forms.user_form import UserCreateForm

class UserService:
    pass

    def get_user_info(self):
        pass
    
    def set_user_info(self):
        pass

    def delete_user(self):
        pass

    def create_user(request):
        if request.method == 'POST':
            form = UserCreateForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                user_image = UserImage(image=request.POST['image'], user=user)
                user_image.save()
                return redirect('user-index')
        else:
            form = UserCreateForm()
        return render(request, 'user/create_user.html',  {
            'form': form
        })
