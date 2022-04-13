from django.db import models

class Pessoa(models.Model):
    class Meta:
        app_label = 'passagens'

    nome = models.CharField(max_length=200)
    email = models.EmailField()