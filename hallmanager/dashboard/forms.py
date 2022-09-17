from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['startTime','endTime','reason','poster','permLetter']
        widgets = {
            'startTime': forms.DateInput(attrs={'type': 'date'}),
            'endTime': forms.DateInput(attrs={'type': 'date'}),
        }