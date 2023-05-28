from django.urls import path
from licitagil import views


urlpatterns = [
    path('', views.index, name='index'),
    path('andamento/', views.LicitacoesEmAndamento.as_view(), name='andamento'),
    path('futuras/', views.LicitacoesFuturas.as_view(), name='futuras'),
    path('ganhas/', views.LicitacoesGanhas.as_view(), name='ganhas'),
]
