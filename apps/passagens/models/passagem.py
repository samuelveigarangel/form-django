from django.db import models
from apps.passagens.models.classe_viagem import ClasseViagem


class Passagem(models.Model):
    class Meta:
        app_label = 'passagens'

    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    data_pesquisa = models.DateField()
    classe_viagem = models.CharField(max_length=100, choices=ClasseViagem.choices, default=0)
    informacoes = models.TextField(max_length=200, blank=True)
