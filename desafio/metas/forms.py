from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NovaMetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ('title', 'description', 'setor', 'responsavel', 'membros', 'entrega')
        widgets = {
            'entrega': DateInput(attrs={'type': 'date'})
        }

class NovoComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('user', 'oquefoifeito', 'oquevaiserfeito', 'impedimento')
