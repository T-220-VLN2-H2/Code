from django.shortcuts import render
from core.forms.checkout_form import PersonalInfoCreateForm
from core.services.checkout_service import CheckoutService


def personal_info(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    if request.method == "POST":
        form = PersonalInfoCreateForm(request.post)
        if form.is_valid():
            new_personl_info = form.save()
    return render(request, "checkout/personal_info.html", context=ctx)


def delivery_info(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    return render(request, "checkout/summary.html", context=ctx)


def payment_info(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    return render(request, "checkout/payment_info.html", context=ctx)


def summary_display(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    return render(request, "checkout/summary.html", context=ctx)
