from django import forms
from jpconnect.models import Employees

class SearchForm(forms.ModelForm):
    result = forms.CharField(max_length=128, help_text="Please enter a last name.")

    class Meta:
        model = Employees
        fields = ('last_name',)