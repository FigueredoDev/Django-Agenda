from django.shortcuts import render
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()     # Coletando dados do banco
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
