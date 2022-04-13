from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .validation import *
from .models import Passagem, Pessoa, ClasseViagem

class PassagemForms(forms.ModelForm):
    class Meta:
        model = Passagem
        fields = '__all__'

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        verifica_data(data_ida, data_volta, data_pesquisa, lista_de_erros)
        verifica_data_pesquisa(data_ida, data_volta, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

