from django import forms
from django.forms import modelformset_factory

from engine.models import Schema


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['name', 'data_name', 'data_type', 'order']

SchemaFormSet = modelformset_factory(
    Schema, fields=("name", "data_name", 'data_type', 'order'), extra=1
)
