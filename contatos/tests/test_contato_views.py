from contatos import views
from django.test import TestCase
from django.urls import resolve, reverse


class TestContatosView(TestCase):
    def test_contatos_index_view_function_is_correct(self):
        view_index = resolve(reverse('contatos:index'))
        self.assertIs(view_index.func, views.index)

    def test_contatos_busca_view_function_is_correct(self):
        view_busca = resolve(reverse('contatos:busca'))
        self.assertIs(view_busca.func, views.busca)

    def test_contatos_detalhes_view_function_is_correct(self):
        view_detalhes = resolve(reverse(
            'contatos:detalhes', kwargs={'contato_id': 1}))
        self.assertIs(view_detalhes.func, views.detalhes)

    def test_contatos_detalhes_view_return_status_code_200_OK(self):
        response = self.client.get(
            reverse('contatos:detalhes', kwargs={'contato_id': 1}))
        self.assertEqual(response.status_code, 404)
