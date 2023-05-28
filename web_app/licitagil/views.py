from django.shortcuts import render
from django.views import generic

# Create your views here.
from licitagil.models import Licitacao

def index(request):
    context = {'saudacao': "Bem vindo ao Sistema Licitágil"}
    return render(request, 'index.html', context=context)

def andamento(request):
    return render(request, 'andamento.html', context)

def futuras(request):
    return render(request, 'futuras.html', context=context)

def ganhas(request):
    return render(request, 'ganhas.html', context=context)

class LicitacoesEmAndamento(generic.ListView):
    model = Licitacao
    context_object_name = 'licitacoes_em_andamento'
    queryset = Licitacao.objects.filter(disputa=True)
    template_name = 'andamento.html'
    paginate_by = 10

class LicitacoesFuturas(generic.ListView):
    model = Licitacao
    context_object_name = 'licitacoes_futuras'
    queryset = Licitacao.objects.filter(disputa=False, ganhou=False)
    template_name = 'futuras.html'
    paginate_by = 10

class LicitacoesGanhas(generic.ListView):
    model = Licitacao
    context_object_name = 'licitacoes_ganhas'
    queryset = Licitacao.objects.filter(ganhou=True)
    template_name = 'ganhas.html'
    paginate_by = 10
