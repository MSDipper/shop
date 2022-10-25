from orders.models import Order
from django import forms
from captcha.fields import CaptchaField


class OrderCreateForm(forms.ModelForm):
    captcha = CaptchaField(
                label='Введите информацию с картинки',
                error_messages={'invalid':'Неправильный ввод'}
                )
    
    class Meta:
        model = Order
        
        fields = [
                'first_name',
                'last_name', 
                'company_name',
                'phone', 
                'address',
                'city'
                  ]
        widgets = {
                "first_name": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Имя",
                        'class': "form-control"
                    }
                ),
                "last_name": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Фамилия",
                        'class': "form-control"
                    }
                ),
                "company_name": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Компания",
                        'class': "form-control"
                    }
                ),
                "phone": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Номер",
                        'class': "form-control"
                    }
                ),
                "address": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Адрес",
                        'class': "form-control"
                    }
                ),
                "city": forms.TextInput(
                    attrs={
                        'type': "text",
                        'placeholder': "Город",
                        'class': "form-control"
                    }
                ),
            }
