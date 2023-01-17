from django import forms


class CouponApplyForm(forms.Form):
    """ Форма ввода кода купона """
    code = forms.CharField(
                        label='',
                        widget=forms.TextInput(attrs={
                                        'class':"gray_btn",
                                        'placeholder':"Coupon Code"
                                        })
                        )
