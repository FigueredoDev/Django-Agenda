from django.contrib import admin
from .models import Categoria, Contato


# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'categoria', 'mostrar')
    list_filter = ('nome', 'categoria')  # Filtros
    list_per_page = 10  # Itens por pagina
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_display_links = ('nome',)
    list_editable = ('mostrar',)


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
