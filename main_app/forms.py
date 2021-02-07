from django import forms
from .models import *

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'number']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['seat', 'items']