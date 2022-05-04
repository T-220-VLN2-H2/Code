class CategoryService:
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

    def delete_category(self):
        pass

    def update_category(self):
        pass