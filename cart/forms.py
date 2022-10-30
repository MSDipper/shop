from django import forms
from shop.models import Product

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    ''' Форма выбора количества и добавление новой суммы к продукту '''
    quantity = forms.IntegerField(min_value=1)
    # # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    