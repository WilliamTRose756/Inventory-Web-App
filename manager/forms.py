from django import forms
from .models import Item



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'lot_number', 'exp_date']



