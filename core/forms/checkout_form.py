from django.forms import ModelForm, widgets
from core.models import PaymentInfo, ShippingDetails


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ["id"]
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
        exclude = ["id", "user"]
        widgets = {
            "full_name": widgets.TextInput(attrs={"class": "form-control"}),
            "address": widgets.TextInput(attrs={"class": "form-control"}),
            "postal_code": widgets.NumberInput(attrs={"class": "form-control"}),
            "city": widgets.TextInput(attrs={"class": "form-control"}),
        }

class DeliveryInfoCreateForm(ModelForm):
    class Meta:
        choices = ["Delivery service", "Pick up", "Postbox", "Speak with seller"]
        exclude = ["id", "user"]
        widgets = {
            "delivery_choice": widgets.RadioSelect(choices=choices)
        }


# class DeliveryInfoCreateForm(ModelForm):
#     class Meta:
#         model
