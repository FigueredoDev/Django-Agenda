from contatos.models import Categoria, Contato
from django.test import TestCase


class ContatoModelsTest(TestCase):
    def setUp(self):
        self.contato = Contato(
            nome="Jhonata", sobrenome="Figueredo", telefone="12334")
        self.categoria = Categoria(nome="Amigos")

    def test_valida_attr_nome(self):
        self.assertEqual(self.contato.nome, "Jhonata")

    def test_valida_attr_sobrenome(self):
        self.assertEqual(self.contato.sobrenome, "Figueredo")

    def test_valida_attr_nome_Categoria(self):
        self.assertEqual(self.categoria.nome, "Amigos")
