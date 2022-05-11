from django.http import QueryDict
from django.shortcuts import render, redirect
from core.forms.checkout_form import PaymentCreateForm, PersonalInfoCreateForm, DeliveryInfoCreateForm
from core.services.checkout_service import CheckoutService
from core.services.bid_service import BidService
from core.models.shipping_details import ShippingDetails
from core.models.payment_info import PaymentInfo


folder_path = "../templates/"


def user(request, bid_id=None):
    ctx = {}
    if request.method == "POST":
        form = PersonalInfoCreateForm(request.POST)
        if form.is_valid():
            request.session["full_name"] = form.cleaned_data["full_name"]
            request.session["address"] = form.cleaned_data["address"]
            request.session["postal_code"] = form.cleaned_data["postal_code"]
            request.session["city"] = form.cleaned_data["city"]
            request.session.modified = True
            return redirect('/checkout/delivery', bid_id)
    elif request.method == "GET":
        print(request.session.keys())
        if len(request.session.keys()) > 3:
            form_init = {}
            form_init["full_name"] = request.session["full_name"]
            form_init["address"] = request.session["address"]
            form_init["postal_code"] = request.session["postal_code"]
            form_init["city"] = request.session["city"]
            form = PersonalInfoCreateForm(form_init)
            ctx["form"] = form
            return render(request, "checkout/user_details.html", context=ctx)
        else:
            form = PersonalInfoCreateForm()
            ctx["form"] = form
            return render(request, "checkout/user_details.html", context=ctx)


def payment(request, bid_id=None):
    ctx = {}
    if request.method == "POST":
        form = PaymentCreateForm(request.POST)
        if form.is_valid():
            request.session["cardholder_name"] = form.cleaned_data["cardholder_name"]
            request.session["card_number"] = form.cleaned_data["card_number"]
            request.session["cvc"] = form.cleaned_data["cvc"]
            request.session["expiry_month"] = form.cleaned_data["expiry_month"]
            request.session["expiry_year"] = form.cleaned_data["expiry_year"]
            request.session.modified = True
            return process_payment(request, bid_id)
    elif request.method == "GET":
        print(request.session.keys())
        if "cardholder_name" in request.session.keys():
            form_init = {}
            form_init["cardholder_name"] = request.session["cardholder_name"]
            form_init["card_number"] = request.session["card_number"]
            form_init["cvc"] = request.session["cvc"]
            form_init["expiry_month"] = request.session["expiry_month"]
            form_init["expiry_year"] = request.session["expiry_year"]
            return render(request, "checkout/payment_info.html", context=ctx)
        else:
            form = PaymentCreateForm()
            ctx["form"] = form
            return render(request, "checkout/payment_info.html", context=ctx)


def delivery(request, bid_id=None):
    ctx = {}
    if request.method == "POST":
        form = DeliveryInfoCreateForm(request.POST)
        if form.is_valid():
            request.session["del_choice"] = form.cleaned_data["del_choice"]
            request.session.modified = True
            return redirect("/checkout/payment", bid_id)
    else:
        form = DeliveryInfoCreateForm()
        ctx["form"] = form
    return render(request, "checkout/delivery_info.html", context=ctx)

def process_payment(request, bid_id):
    bid = BidService.get_bid_by_id(bid_id)
    bid.status = "COMPLETED"
    bid.save()
    if request.method == "POST":
        shipping_details = ShippingDetails(user_info = request.session["full_name"],
                                            address = request.session["address"],
                                            post_code = request.session["post_code"],
                                            city = request.session["city"])
        payment_details = PaymentInfo(cardholder_name = request.session["cardholder_name"],
                                        card_number = request.session["card_number"],
                                        cvc = request.session["cvc"],
                                        expiry_month = request.session["expiry_month"],
                                        expiry_year = request.session["expiry_year"])
        shipping_details.save()
        payment_details.save()

def summary(request):
    ctx = {}
    if request.method == "POST":
        return redirect("index_page")
    return render(request, "checkout/summary.html", context=ctx)


