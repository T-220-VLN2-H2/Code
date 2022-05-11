from django.forms import widgets, ModelForm
from core.models import UserBids


class BidCreateForm(ModelForm):
    class Meta:
        model = UserBids
        fields = ["amount"]
        widgets = {
            "Amount:": widgets.NumberInput(attrs={"class": "form-control"})
            # "Expires": widgets.DateInput(attrs={"class": "form-control"}),
        }
