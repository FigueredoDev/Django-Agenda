from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.detalhes, name='detalhes'), # <int:contato_id> = parametro para a url
]