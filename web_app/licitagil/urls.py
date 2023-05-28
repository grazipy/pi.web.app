from django.urls import path
from licitagil import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ganhas/', views.LicitacoesGanhas.as_view(), name='ganhas'),
]
