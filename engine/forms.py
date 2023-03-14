from django import forms
from django.forms import modelformset_factory

from engine.models import Schema, Data


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['name']


DataFormSet = modelformset_factory(Data, fields=("data_name", 'data_type', 'order'), extra=1)
