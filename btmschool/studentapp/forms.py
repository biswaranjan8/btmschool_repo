from django import forms
from .models import registerModel


class rgdForm(forms.ModelForm):
    class Meta:
        model = registerModel
        fields = '__all__'
        widgets = {

            'DOB': forms.DateInput(),
            'gender': forms.RadioSelect(),
            'caste': forms.RadioSelect(),
            'blood_group': forms.RadioSelect(),

        }
