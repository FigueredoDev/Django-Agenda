from .models import Contato
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    contatos = Contato.objects.all()  # Coletando dados do banco
    paginator = Paginator(contatos, 10)  # Show 10 contacts per page
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
