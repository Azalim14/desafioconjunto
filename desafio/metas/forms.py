from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NovaMetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ('titulo', 'descricao', 'setor', 'responsavel', 'membros', 'entrega')
        widgets = {
            'entrega': DateInput(attrs={'type': 'date'})
        }

class NovaMetaSetorForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ('titulo', 'descricao', 'responsavel', 'membros', 'entrega')
        widgets = {
            'entrega': DateInput(attrs={'type': 'date'})
        }

class NovoComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('usuario', 'oquefoifeito', 'oquevaiserfeito', 'impedimento')

class AlterandoPorcentagemForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ('porcentagem', )