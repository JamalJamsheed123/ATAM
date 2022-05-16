from re import X
from django import forms
from django.forms import fields
from AssetRegistration.models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields="__all__"