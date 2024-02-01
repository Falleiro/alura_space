from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário'
        }

        widgets = {
            'nome':forms.TextInput(attrs={'class': 'fomr-control'}),
            'legenda':forms.TextInput(attrs={'class': 'fomr-control'}),
            'categoria':forms.Select(attrs={'class': 'fomr-control'}),
            'descricao':forms.Textarea(attrs={'class': 'fomr-control'}),
            'foto':forms.FileInput(attrs={'class': 'fomr-control'}),
            'data_fotografia':forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'fomr-control'
                    }
                ),
            'usuario':forms.Select(attrs={'class': 'fomr-control'}),
        }
