from django import forms
from django.forms import ModelForm, widgets
from django import forms
from models.users import User

class UserCreateForm(ModelForm):
    image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'sub_categories': widgets.TextInput(attrs={'class': 'form-control'}),
        }

