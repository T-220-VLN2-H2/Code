from django.shortcuts import render
from core.forms.checkout_form import PaymentCreateForm, PersonalInfoCreateForm
from core.services.checkout_service import CheckoutService


folder_path = "../templates/"


def user(request):
    ctx = {
        "full_name": "",
        "address": "",
    }
    if request.method == "POST":
        form = PersonalInfoCreateForm(request.POST)
        request.session["full_name"] = form["full_name"]
        request.session["address"] = form["address"]
        request.session["postal_code"] = form["postal_code"]
        request.session["city"] = form["city"]
        request.session.modified = True
    else:
        form = PersonalInfoCreateForm()
        ctx["form"] = form
    return render(request, "checkout/user_details.html", context=ctx)


def delivery(request):
    ctx = {
        "full_name": "",
        "address": "",
    }
    if request.method == "POST":
        form = PaymentCreateForm(request.POST)
    else:
        form = PaymentCreateForm()
        ctx["form"] = form
    return render(request, "checkout/payment.html", context=ctx)


def payment(request):
    ctx = {
        "cardholder_name": "",
        "card_number": "",
        "cvc": "",
        "expiry_month": "",
    }
    if request.method == "POST":
        form = PaymentCreateForm(request.POST)
        request.session["cardholder_name"] = form["cardholder_name"]
        request.session["card_number"] = form["card_number"]
        request.session["cvc"] = form["cvc"]
        request.session["expiry_month"] = form["expiry_year"]
        request.session.modified = True
    else:
        form = PaymentCreateForm()
        ctx["form"] = form
    return render(request, "checkout/payment_info.html", context=ctx)


def summary(request):
    ctx = {
        "full_name": "",
        "address": "",
    }
    return render(request, "checkout/summary.html", context=ctx)
