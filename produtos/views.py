from django.shortcuts import render
from produtos.models import *

def index(request):
	produtos = Produto.objects.filter(disponivel=True)
	tipos = Tipo.objects.all()
	categorias = Categoria.objects.all()
	return render(request, 'produtos/index.html', {'categoria_loja': 'Moda Íntima',
    												'nome_loja': 'Madame Chique',
    												'produtos': produtos,
    												'categorias': categorias,
    												'tipos': tipos,
    												})
