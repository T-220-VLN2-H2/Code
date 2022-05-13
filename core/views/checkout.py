from ast import Or
import re
from django.shortcuts import render, redirect
from core.forms.checkout_form import (
    PaymentCreateForm,
    PersonalInfoCreateForm,
    DeliveryInfoCreateForm,
)
from core.services.checkout_service import CheckoutService
from core.services.bid_service import BidService
from core.services.item_service import ItemService
from core.services.order_service import OrderService
from core.models.shipping_details import ShippingDetails
from core.models.payment_info import PaymentInfo
from core.models.order import Order
from datetime import date


def user(request, item_id=None):
    print(request.method)
    if request.method == "POST":
        form = PersonalInfoCreateForm(request.POST)
        if form.is_valid():
            request.session["full_name"] = form.cleaned_data["full_name"]
            request.session["address"] = form.cleaned_data["address"]
            request.session["postal_code"] = form.cleaned_data["postal_code"]
            request.session["city"] = form.cleaned_data["city"]
            request.session["country"] = form.cleaned_data["country"]
            request.session.modified = True
            return redirect("/checkout/payment", item_id)
        else:
            form = PersonalInfoCreateForm()
            ctx = {}
            ctx["form"] = form
            request.session["item_id"] = request.POST.get("bid")
            request.session.modified = True
        return render(request, "checkout/user_details.html", context=ctx)
    elif request.method == "GET":
        if len(request.session.keys()) > 3:
            form_init = {}
            form_init["full_name"] = request.session["full_name"]
            form_init["address"] = request.session["address"]
            form_init["postal_code"] = request.session["postal_code"]
            form_init["city"] = request.session["city"]
            form_init["country"] = request.session["country"]
            form = PersonalInfoCreateForm(form_init)
            ctx = {}
            ctx["form"] = form
            return render(request, "checkout/user_details.html", context=ctx)



def payment(request):
    print(request.method)
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
            return process_payment(request)
        else:
            form = PaymentCreateForm()
            ctx = {}
            ctx["form"] = form
            request.session["item_id"] = request.POST.get("bid")
            request.session.modified = True
        return render(request, "checkout/payment_info.html", context=ctx)
    elif request.method == "GET":
        if "cardholder_name" in request.session.keys():
            form_init = {}
            form_init["cardholder_name"] = request.session["cardholder_name"]
            form_init["card_number"] = request.session["card_number"]
            form_init["cvc"] = request.session["cvc"]
            form_init["expiry_month"] = request.session["expiry_month"]
            form_init["expiry_year"] = request.session["expiry_year"]
            form = PaymentCreateForm(form_init)
            ctx["form"] = form
            return render(request, "checkout/payment_info.html", context=ctx)
        else:
            form = PaymentCreateForm()
            ctx["form"] = form
            return render(request, "checkout/payment_info.html", context=ctx)


def process_payment(request):
    print(request.method)
    if request.method == "POST":
        shipping_details = ShippingDetails(
            full_name=request.session["full_name"],
            address=request.session["address"],
            postal_code=request.session["postal_code"],
            city=request.session["city"],
            country=request.session["country"],
        )
        payment_details = PaymentInfo(
            cardholder_name=request.session["cardholder_name"],
            card_number=request.session["card_number"],
            cvc=request.session["cvc"],
            expiry_month=request.session["expiry_month"],
            expiry_year=request.session["expiry_year"],
        )
        shipping_details.save()
        payment_details.save()
        summary_details_dict = {}
        summary_details_dict["full_name"] = request.session["full_name"]
        summary_details_dict["address"] = request.session["address"]
        summary_details_dict["postal_code"] = request.session["postal_code"]
        summary_details_dict["city"] = request.session["city"]
        summary_details_dict["cardholder_name"] = request.session["cardholder_name"]
        summary_details_dict["card_number"] = request.session["card_number"]
        summary_details_dict["cvc"] = request.session["cvc"]
        summary_details_dict["expiry_month"] = request.session["expiry_month"]
        summary_details_dict["expiry_year"] = request.session["expiry_year"]
        request.session["summary_details"] = summary_details_dict
        return redirect("/checkout/summary")

def summary(request):
    print(request.method)
    ctx = {}
    #if "bid_id" in request.session.keys():
    if request.method == "GET":
        summary_details = request.session["summary_details"]
        date_today = date.today()
        bid = BidService.get_accepted_bid_by_item_id(request.session["item_id"])
        item = ItemService.get_item_by_id(request.session["item_id"])
        request.session["bid_id"] = bid.id
        request.session["buyer_id"] = bid.user_id_id
        request.session["seller_id"] = item.seller_id
        request.session["item_id"] = item.id
        request.session.modified = True
        ctx["price"] = bid.amount
        ctx["item_name"] = item.title
        ctx["summary"] = summary_details
        ctx["date"] = date_today
        return render(request, "checkout/summary.html", context=ctx)
    else:
        OrderService.create_order(request.session["buyer_id"], request.session["item_id"], request.session["seller_id"])
        bid = BidService.get_bid_by_id(request.session["bid_id"])
        request.session["bid_id"] = bid.id
        bid.status = "COMPLETED"
        bid.save()
        for key in list(request.session.keys()):
            if not key.startswith("_"): # skip keys set by the django system
                del request.session[key]
        return redirect("index_page")
