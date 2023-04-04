from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import modelformset_factory, TextInput, ChoiceField, NumberInput, Select

from engine.models import Schema, Data, CHOICES


class SchemaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control col-3'}))

    class Meta:
        model = Schema
        fields = ['name']

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


DataFormSet = modelformset_factory(Data,
                                   fields=("data_name", 'data_type', 'order'),
                                   widgets={'data_name': TextInput(attrs={'class': 'form-control col-3'}),
                                            'data_type': Select(choices=CHOICES,attrs={'class': 'form-control col-3'}),
                                            'order': NumberInput(attrs={'class': 'form-control col-3'})},
                                   extra=1)
