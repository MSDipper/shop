from django import forms
from shop.models import Product


class CartAddProductForm(forms.Form):
    ''' Форма выбора количества и добавление новой суммы к продукту '''
    quantity = forms.IntegerField(min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    
