from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, )
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today())

    classe_voo = [('Primeira Classe', 'Primeira Classe'), ('Executiva', 'Executiva'), ('Econômica', 'Econômica')]
    escolha_classe = forms.ChoiceField(label='Classe de vôo ', widget=forms.Select(), choices=classe_voo, initial='Primeira Classe')
    informacoes = forms.CharField(label='Observações', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=150)
