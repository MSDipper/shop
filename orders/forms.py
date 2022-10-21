from orders.models import OrderItemList
from django import forms

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderItemList
        fields = '__all__'