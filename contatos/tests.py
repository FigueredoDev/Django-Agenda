from django.test import TestCase  # noqa: F401
from django.urls import reverse

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
    def test_contato_url_index_esta_correta(self):
        index_url = reverse('contatos:index')
        self.assertEqual(index_url, '/')

    def test_contato_url_busca_esta_correta(self):
        busca_url = reverse('contatos:busca')
        self.assertEqual(busca_url, '/busca/')
