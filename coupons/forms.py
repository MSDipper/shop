from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        label='Код с купона',
        widget=forms.TextInput(attrs={'class':"gray_btn"})
        )