from django.urls import path

from . import views

app_name = 'contatos'

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.detalhes, name='detalhes')
]
