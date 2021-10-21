from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
