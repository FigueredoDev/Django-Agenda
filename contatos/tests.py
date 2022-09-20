from django.test import TestCase  # noqa: F401
from django.urls import resolve, reverse

from . import views
# Create your tests here.
from .models import Categoria, Contato  # noqa: F401


class ContatoModelsTest(TestCase):
    def setUp(self) -> None:
        self.contato = Contato(
            nome="Jhonata", sobrenome="Figueredo", telefone="12334")
        self.categoria = Categoria(nome="Amigos")

    def test_valida_attr_nome(self):
        self.assertEqual(self.contato.nome, "Jhonata")

    def test_valida_attr_sobrenome(self):
        self.assertEqual(self.contato.sobrenome, "Figueredo")

    def test_valida_attr_nome_Categoria(self):
        self.assertEqual(self.categoria.nome, "Amigos")


class TestContatoURLs(TestCase):
    def test_contatos_url_index_is_correct(self):
        index_url = reverse('contatos:index')
        self.assertEqual(index_url, '/')

    def test_contatos_url_busca_is_correct(self):
        busca_url = reverse('contatos:busca')
        self.assertEqual(busca_url, '/busca/')

    def test_contatos_url_detalhes_is_correct(self):
        detalhes_url = reverse('contatos:detalhes', kwargs={'contato_id': 1})
        self.assertEqual(detalhes_url, '/1')


class TestContatosView(TestCase):
    def test_contatos_index_view_function_is_correct(self):
        view_index = resolve(reverse('contatos:index'))
        self.assertIs(view_index.func, views.index)

    def test_contatos_busca_view_function_is_correct(self):
        view_busca = resolve(reverse('contatos:busca'))
        self.assertIs(view_busca.func, views.busca)

    def test_contatos_detalhes_view_function_is_correct(self):
        view_detalhes = resolve(reverse(
            'contatos:detalhes', kwargs={'contato_id': 1})
        )
        self.assertIs(view_detalhes.func, views.detalhes)
