from django import forms
from django.contrib.auth.models import User
from .models import imagefiled, newspage


class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class galleryform(forms.ModelForm):
    class Meta:
        model = imagefiled
        fields = "__all__"


class newsform(forms.ModelForm):
    class Meta:
        model = newspage
        fields = "__all__"
