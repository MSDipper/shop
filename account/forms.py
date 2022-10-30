
from django import forms



class AuthenticationForm(forms.Form):
    email = forms.EmailInput()
    password = forms.PasswordInput()
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':"form-control",'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class':"form-control",'placeholder': 'Password'})
        
    