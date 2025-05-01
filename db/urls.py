# meu_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('erros/', views.listar_erros_view, name='listar_erros'),
    path('corrigir/<str:schema>/<str:tabela>/<int:id_rotina>/', views.corrigir_erro_view, name='corrigir_erro'),
]
