from django.forms import widgets
from core.models import Item

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'Price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Condition': widgets.CheckboxInput(attrs={'class': 'form-control'}),
            'Category': widgets.Select(attrs={'class': 'form-control'}),
            'Delivery_Options': widgets.Select(attrs={'class': 'form-control'})
        }