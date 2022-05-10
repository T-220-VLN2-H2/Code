from django.forms import ModelForm, widgets
from core.models import Order
from django.forms import modelformset_factory

WIDGETS = {
            "item": widgets.TextInput(attrs={'readonly': 'readonly'}),
            "buyer": widgets.TextInput(attrs={'readonly': 'readonly'}),
            "seller": widgets.TextInput(attrs={'readonly': 'readonly'}),
            "rating": widgets.RadioSelect(attrs={'class': 'd-flex'}),
        }

OrderForm = modelformset_factory(Order, fields=['item', 'buyer', 'seller', 'rating'], widgets=WIDGETS)




# class OrderRatingForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ["rating"]
#         exclude = ['seller', 'buyer', 'item']
#         widgets = {
#             "rating": widgets.RadioSelect(attrs={'class': 'd-flex'})
#         }
