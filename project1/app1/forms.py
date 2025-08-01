from django import forms
from .models import election

class add_details(forms.ModelForm):
    class Meta:
        model=election
        fields=['name','father_name','date_of_birth','house_name','ward_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select a date'
            }),
        }