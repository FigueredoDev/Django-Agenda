from django.http import Http404, HttpResponse

from .models import Contato
from django.shortcuts import render, get_object_or_404
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
    campos = Concat('nome', Value(' '), 'sobrenome')

    if termo is None or not termo:
        return HttpResponse('''<p>
    Campo vazio, insira dados para busca!
    <br>
    <a href="/">Retornar ao inicio</a>
    </p>''')

    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 20)  # Show 10 contacts per page
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

