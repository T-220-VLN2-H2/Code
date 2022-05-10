from django.shortcuts import render
from core.forms.checkout_form import PaymentCreateForm, PersonalInfoCreateForm
from core.services.checkout_service import CheckoutService


def user(request):
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
    else:
        form = PersonalInfoCreateForm()
        ctx["form"] = form
    return render(request, "checkout/user_details.html", context=ctx)


def delivery(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    if request.method == "POST":
        form = PaymentCreateForm(request.post)
        if form.is_valid():
            new_personl_info = form.save()
    else:
        form = PaymentCreateForm()
        ctx["form"] = form
    return render(request, "checkout/payment.html", context=ctx)


def payment(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    if request.method == "POST":
        form = PaymentCreateForm(request.post)
        if form.is_valid():
            new_personl_info = form.save()
    else:
        form = PaymentCreateForm()
        ctx["form"] = form
    return render(request, "checkout/payment_info.html", context=ctx)


def summary(request):
    folder_path = "../templates/"
    checkout_service = CheckoutService()
    ctx = {
        "full_name": "",
        "address": "",
    }
    return render(request, "checkout/summary.html", context=ctx)
