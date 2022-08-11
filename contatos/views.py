from django.shortcuts import render
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()  # Coletando dados do banco
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
