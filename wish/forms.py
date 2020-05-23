from django import forms
from django.forms.widgets import DateInput

from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['name','email','birth_date','wish']
        widgets = {'birthday_date': DateInput()}