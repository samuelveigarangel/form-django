from django.shortcuts import render
from ..forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {
        'form': form,
        'pessoa_form': pessoa_form
    }
    return render(request, 'passagem/index.html', contexto)
