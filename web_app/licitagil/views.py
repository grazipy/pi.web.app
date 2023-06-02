from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from licitagil.models import Licitacao

def index(request):
    context = {'saudacao': "Bem vindo ao Sistema Licitágil! Selecione uma opção no menu."}
    return render(request, 'index.html', context=context)

def andamento(request):
    return render(request, 'andamento.html', context)

def futuras(request):
    return render(request, 'futuras.html', context)

def ganhas(request):
    return render(request, 'ganhas.html', context)

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

class CadastrarLicitacao(CreateView):
    model = Licitacao
    fields = '__all__'

class EditarLicitacao(UpdateView):
    model = Licitacao
    fields = '__all__'

class ExcluirLicitacao(DeleteView):
    model = Licitacao
    success_url = reverse_lazy('andamento')
