from django.shortcuts import render
from ..forms import PassagemForms


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