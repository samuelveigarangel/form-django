from django.shortcuts import render, redirect
from ..forms import PassagemForms


def index(request):
    form = PassagemForms()
    contexto = {
        'form': form
    }
    return render(request, 'passagem/index.html', contexto)


def consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.   POST)
        if form.is_valid():
            contexto = {
                'form': form
            }
            return render(request, 'passagem/consulta.html', contexto)
        else:
            contexto = {
                'form':form
            }
            return render(request, 'passagem/index.html', contexto)