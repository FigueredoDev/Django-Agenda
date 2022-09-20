from django.test import TestCase
from django.urls import reverse


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
