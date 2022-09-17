from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['startTime','endTime','reason','poster','permLetter']
        widgets = {
            'startTime': forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type': 'datetime-local'}),
            'endTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }