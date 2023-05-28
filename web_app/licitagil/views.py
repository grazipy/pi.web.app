from django.shortcuts import render
from django.views import generic

# Create your views here.
from licitagil.models import Licitacao

def index(request):
    context = {'saudacao': "Bem vindo ao Sistema Licitágil"}
    return render(request, 'index.html', context=context)

def ganhas(request):
    context = {
        licitacoes_ganhas == Licitacao.objects.filter(ganhou=True)
    }
    return render(request, 'ganhas.html', context=context)

class LicitacoesGanhas(generic.ListView):
    model = Licitacao
    context_object_name = 'licitacoes_ganhas'
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'ganhas.html'
    paginate_by = 10