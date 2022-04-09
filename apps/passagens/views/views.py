from django.shortcuts import render
from ..forms import PassagemForms


def index(request):
    form = PassagemForms()

    contexto = {
        'form': form
    }

    return render(request, 'passagem/index.html', contexto)


def consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        contexto = {
            'form': form
        }

        return render(request, 'passagem/consulta.html', contexto)