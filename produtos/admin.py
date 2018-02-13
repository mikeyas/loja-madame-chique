from django.contrib import admin
from .models import *
from .forms import *


class ProdutoAdmin (admin.ModelAdmin):
	form = ProdutoForm
	list_display = ['__str__', 'preco', 'tipo', 'categoria',]
	search_fields = ['nome', 'slug', 'descricao', 'detalhe']
	prepopulated_fields = {'slug':('tipo', 'nome',)}
	FotoProduto.foto

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Tamanho)
admin.site.register(Cor)
admin.site.register(FotoProduto)

