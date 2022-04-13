from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .validation import campo_tem_algum_numero, origem_destino_iguais

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, )
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today())

    classe_voo = [('Primeira Classe', 'Primeira Classe'), ('Executiva', 'Executiva'), ('Econômica', 'Econômica')]
    escolha_classe = forms.ChoiceField(label='Classe de vôo ', widget=forms.Select(), choices=classe_voo, initial='Primeira Classe')
    informacoes = forms.CharField(label='Observações', max_length=200, widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=150, required=False)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        print(lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

