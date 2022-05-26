from datetime import datetime
from django import forms
from agenda.models import Compromisso
from django.core.exceptions import ValidationError
class CompromissoForm(forms.ModelForm):
    data_registro = forms.DateTimeField(widget=forms.DateTimeInput())
    def cleaned_data(self):
        data = self.cleaned_data['data']
        data_registro = self.cleaned_data['data_registro']
        if datetime(data) < datetime(data_registro):
            self.add_error('data', ValidationError('A data do compromisso não pode ser menor que a data de hoje.'))
        return data

    data_registro = forms.DateTimeField(widget=forms.DateTimeInput(), initial=datetime.now)
    class Meta:
        model = Compromisso
        fields = ['titulo', 'data', 'descricao']
        labels = {'titulo': 'Título', 'data': 'Data do Compromisso', 'descricao': 'Descrição do Compromisso'}
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'data': forms.DateTimeInput(),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'required': True})
        }

