from django import forms
from apps.models import Carbonad


class CarbonadForm(forms.ModelForm):
    class Meta:
        model = Carbonad
        fields = '__all__'
