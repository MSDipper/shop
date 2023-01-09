from django import forms
from blog.models import Comment
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CommentPostForm(forms.ModelForm):
    captcha = ReCaptchaField(
                widget=ReCaptchaV2Checkbox,
                error_messages={'invalid':'Повторите'}
                )
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')
        widgets = {
                'name': forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Your Full name'}),
                'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder': 'Email Address'}),
                'message': forms.Textarea(attrs={'class':"form-control", 'placeholder': 'Message', 'id':'commentblog'})
            }