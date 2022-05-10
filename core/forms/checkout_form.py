from django.forms import ModelForm, widgets
from core.models import PaymentInfo, ShippingDetails


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInfo
        fields = [
            "cardholder_name",
            "card_number",
            "cvc",
            "expiry_month",
            "expiry_year",
        ]
        widgets = {
            "cardholder_name": widgets.TextInput(attrs={"class": "form-control"}),
            "card_number": widgets.TextInput(attrs={"class": "form-control"}),
            "cvc": widgets.TextInput(attrs={"class": "form-control"}),
            "expiry_month": widgets.NumberInput(attrs={"class": "form-control"}),
            "expiry_year": widgets.NumberInput(attrs={"class": "form-control"}),
        }


class PersonalInfoCreateForm(ModelForm):
    class Meta:
        model = ShippingDetails
        fields = ["full_name", "address", "postal_code", "city"]
        widgets = {
            "full_name": widgets.TextInput(attrs={"class": "form-control"}),
            "address": widgets.TextInput(attrs={"class": "form-control"}),
            "postal_code": widgets.NumberInput(attrs={"class": "form-control"}),
            "city": widgets.TextInput(attrs={"class": "form-control"}),
        }

# class DeliveryInfoCreateForm(ModelForm):
#     class Meta:
#         model 