from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['startTime','endTime','reason']
        widgets = {
            'startTime': forms.DateTimeInput(format='%Y-%M-%D %H:%M', attrs={'type': 'datetime-local'}),
            'endTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }