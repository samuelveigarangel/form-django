from django.urls import path
from apps.passagens.views import *

urlpatterns = [
    path('', index, name='index'),
    path('consulta', consulta, name='consulta')

]