from django import forms
import sys
from pathlib import Path

class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, help_text='100 characters max!')
    email = forms.CharField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)