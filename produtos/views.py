from django.shortcuts import render, get_object_or_404
from produtos.models import *
from pagseguro.api import PagSeguroItem, PagSeguroApi
from django.core import serializers

def index(request):
	template = 'home/index.html'
	produtos = Produto.objects.filter(disponivel=True)
	tipos = Tipo.objects.all()
	categorias = Categoria.objects.all()
	return render(request, template, 	{'categoria_loja': 'Moda Íntima',
										'nome_loja': 'Madame Chique',
										'produtos': produtos,
										'categorias': categorias,
										'tipos': tipos,
										})

def produto(request, slug):
	template = 'produtos/produto.html'
	produto = get_object_or_404(Produto, disponivel=True, slug=slug)
	tipos = Tipo.objects.all()
	categorias = Categoria.objects.all()
	return render(request, template, 	{'categoria_loja': 'Moda Íntima',
										'nome_loja': 'Madame Chique',
										'produto': produto,
										'categorias': categorias,
										'tipos': tipos,
										})

def searchTipoCategoria(request, cod_cat=None, cod_tipo=None):
	template = 'home/index.html'
	produtos = Produto.objects.filter(disponivel=True, tipo=cod_tipo, categoria=cod_cat)
	tipos = Tipo.objects.all()
	categorias = Categoria.objects.all()
	return render(request, template, 	{'categoria_loja': 'Moda Íntima',
										'nome_loja': 'Madame Chique',
										'produtos': produtos,
										'categorias': categorias,
										'tipos': tipos,
										})

def carrinho(request, cod_produto=None):
	template = 'produtos/carrinho.html'
	produtos = Produto.objects.filter(disponivel=True)
	tipos = Tipo.objects.all()
	categorias = Categoria.objects.all()
	request.session.set_expiry(0)
	carrinho = []
	if cod_produto:
		p = Produto.objects.get(codigo=cod_produto)
		produto = {
					'produto': p.nome,
					'ref': p.referencia,
					'cor': 'azul',
					'tamanho': 'M',
					'quantidade': 1,
					'preco': p.preco,
					'total': p.preco*1,
				  }
		if 'carrinho' in request.session:
			carrinho = request.session.get('carrinho')
		carrinho.append(produto)
		print (len(carrinho))
		request.session['carrinho'] = carrinho
		template = 'home/index.html'
	return render(request, template, 	{'categoria_loja': 'Moda Íntima',
										'nome_loja': 'Madame Chique',
										'produtos': produtos,
										'categorias': categorias,
										'tipos': tipos,
										})

