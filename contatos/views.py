from django.shortcuts import render, get_object_or_404
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()  # Coletando dados do banco
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
