from django.shortcuts import render
from ..forms import PassagemForms, PessoaForms


def consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoaForm = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form,
                'pessoaForm': pessoaForm
            }
            return render(request, 'passagem/consulta.html', contexto)
        else:
            contexto = {
                'form':form,
                'pessoaForm': pessoaForm
            }
            return render(request, 'passagem/index.html', contexto)