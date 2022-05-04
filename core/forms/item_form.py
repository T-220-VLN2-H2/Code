from django.forms import ModelForm, widgets
from core.models import Item

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'Price': widgets.TextInput(attrs={'class': 'form-control'}),
            'Condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'Category': widgets.TextInput(attrs={'class': 'form-control'})
        }

class 