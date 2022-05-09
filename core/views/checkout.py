from django.shortcuts import render
from core.forms.checkout_form import PersonalInfoCreateForm
from core.services.checkout_service import CheckoutService

folder_path = "../templates/"
checkout_service = CheckoutService()
ctx = {
    "full_name": "",
    "address": "",
}

# def register(request):
#     if request.user.is_authenticated:
#         return redirect("user_home")
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = UserCreationForm(request.POST)
#         # check whether it's valid:

#         if form.is_valid():
#             new_user = form.save()
#             new_user.refresh_from_db()  # load the profile instance created by the signal
#             new_user.profile.birth_date = form.cleaned_data.get("birth_date")
#             new_user.save()
#             raw_password = form.cleaned_data.get("password1")
#             new_user = authenticate(username=new_user.username, password=raw_password)
#             ctx["user"] = new_user
#             login(request, new_user)
#             return redirect("user_home")
#         ctx["form"] = form
#     else:
#         ctx["form"] = UserCreationForm
#     return render(request, f"{folder_path}/register.html", context=ctx)

def personal_info(request):
    if request.method == "POST":
        form = PersonalInfoCreateForm(request.post)
        if form.is_valid():
            new_personl_info = form.save()
    return render(request, "checkout/personal_info.html", context=ctx)

def delivery_info(request):
    return render(request, "checkout/summary.html", context=ctx)

def payment_info(request):
    return render(request, "checkout/payment_info.html", context=ctx)

def summary_display(request):
    return render(request, "checkout/summary.html", context=ctx)