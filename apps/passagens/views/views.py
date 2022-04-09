from django.shortcuts import render
from ..forms import PassagemForms


def index(request):
    form = PassagemForms()

    contexto = {
        'form': form
    }

    return render(request, 'passagem/index.html', contexto)
