from django.forms import ModelForm, widgets
from core.models import Payment, shipping

class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInformation
        widgets = {
            'Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'Card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'Cvc': widgets.TextInput(attrs={'class': 'form-control'}),
            'Expiry_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Expiry_year' : widgets.NumberInput(attrs={'class': 'form-control'})
        }

class ShippingCreateForm(ModelForm):
    class Meta:
        model = ShippingInformation
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }