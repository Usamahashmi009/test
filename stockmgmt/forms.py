# forms.py
from django import forms
from .models import Stock, ItemSize,Company,Vender
from django.forms import formset_factory


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item_size', 'quantity', 'rate', 'company']
        


StockCreateFormSet = formset_factory(StockCreateForm, extra=5)

class AddItemSizeForm(forms.ModelForm):
    class Meta:
        model = ItemSize
        fields = ['name']

class AddItemCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class AddVenderForm(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ['name']