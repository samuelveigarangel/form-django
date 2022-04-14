from django.shortcuts import render
from ..forms import PassagemForms, PessoaForms


def consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form,
                'pessoaForm': pessoa_form
            }
            return render(request, 'passagem/consulta.html', contexto)
        else:
            contexto = {
                'form': form,
                'pessoa_form': pessoa_form
            }
            return render(request, 'passagem/index.html', contexto)
