from django.forms import widgets, ModelForm
from core.models import Item


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ["id", "is_sold", "date_created", "seller", "images"]
        widgets = {
            "Price": widgets.NumberInput(attrs={"class": "form-control"}),
            "Condition": widgets.CheckboxInput(attrs={"class": "form-control"}),
            "Category": widgets.Select(attrs={"class": "form-control"}),
            "Delivery_Options": widgets.Select(attrs={"class": "form-control"}),
            "Description": widgets.Textarea(attrs={"class": "form-control"}),
        }
