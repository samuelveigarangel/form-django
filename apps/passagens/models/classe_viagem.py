from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseViagem(models.TextChoices):
        ECONOMICA = 'ECO', _('Econômica')
        EXECUTIVA = 'EXEC', _('Executiva')
        PRIMEIRA_CLASSE = 'PRIMEIRA', _('Primeira Classe')