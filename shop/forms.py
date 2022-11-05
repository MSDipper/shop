from django import forms
from shop.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'photo', 'message')
        widgets = {
                'name': forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Your Full name'}),
                'email': forms.EmailInput(attrs={'class':"form-control", 'placeholder': 'Email Address'}),
                'message': forms.Textarea(attrs={'class':"form-control", 'placeholder': 'Message'})
            }