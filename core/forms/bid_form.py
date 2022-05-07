from django.forms import widgets, ModelForm
from core.models import UserBids


class BidCreateForm(ModelForm):
    class Meta:
        model = UserBids
        exclude = ["user_id", "item_id", "timestamp", "expires"]
        field = ["amount"]
        widgets = {
            "Amount:": widgets.NumberInput(attrs={"class": "form-control"})
            # "Expires": widgets.DateInput(attrs={"class": "form-control"}),
        }
