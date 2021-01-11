from django import forms
from .models import *

class NovaMetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ('title', 'description')
