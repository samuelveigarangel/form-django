from django.urls import path
from apps.passagens.views import *

urlpatterns = [
    path('', views.index, name='index'),

]