from django.contrib import messages
from django.http import Http404

from .models import Contato
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(contatos, 20)  # Show 10 contacts per page
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo de busca não pode estar vazio!')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 20)  # Show 10 contacts per page
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

