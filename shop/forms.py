from django import forms
from shop.models import Comment, Reviews, Rating, RatingStar
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(
                widget=ReCaptchaV2Checkbox,
                error_messages={'invalid':'Повторите'}
                )
    
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'photo', 'message')
        widgets = {
                'name': forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Your Full name'}),
                'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder': 'Email Address'}),
                'message': forms.Textarea(attrs={'class':"form-control", 'placeholder': 'Message'})
            }


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField(
                widget=ReCaptchaV2Checkbox,
                error_messages={'invalid':'Повторите'}
                )
    
    
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'message')
        widgets = {
                'name': forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Your Full name'}),
                'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder': 'Email Address'}),
                'message': forms.Textarea(attrs={'class':"form-control", 'placeholder': 'Message'})
            }


class RatingForm(forms.ModelForm):
    ''' Форма добавление рейтинга '''
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )
    
    class Meta:
        model = Rating
        fields = ('star',)