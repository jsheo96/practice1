from .models import Location
from django import forms

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude']