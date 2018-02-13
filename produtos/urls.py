from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    #url(r'^produto/(?P<cod_produto>\d+)/$', views.produto, name='produto'),
    url(r'^produto/(?P<slug>[\w_-]+)/$', views.produto, name='produto'),
    url(r'^produto/filtro/(?P<cod_cat>\d+)/(?P<cod_tipo>\d+)/$', views.searchTipoCategoria, name='searchproduto'),
    url(r'^carrinho/$', views.carrinho, name='exibircarrinho'),
    url(r'^carrinho/(?P<cod_produto>\d+)/$', views.carrinho, name='carrinho'),
]