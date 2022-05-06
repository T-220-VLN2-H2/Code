<<<<<<< HEAD
from django.forms import widgets
from django import forms
=======
from django.forms import widgets, ModelForm
>>>>>>> origin/main
from core.models import Item

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
<<<<<<< HEAD
        exclude = ['id']
        image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        widgets = {
            'Price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Condition': widgets.CheckboxInput(attrs={'class': 'form-control'}),
            'Category': widgets.Select(attrs={'class': 'form-control'}),
            'Delivery_Options': widgets.Select(attrs={'class': 'form-control'})
        }
=======
        exclude = ["id", "is_sold", "date_created"]
        widgets = {
            "Price": widgets.NumberInput(attrs={"class": "form-control"}),
            "Condition": widgets.CheckboxInput(attrs={"class": "form-control"}),
            "Category": widgets.Select(attrs={"class": "form-control"}),
            "Delivery_Options": widgets.Select(attrs={"class": "form-control"}),
            "Description": widgets.Textarea(attrs={"class": "form-control"}),
        }
>>>>>>> origin/main
