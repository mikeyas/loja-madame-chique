from django import forms
from django.forms import ModelForm
from .models import *


class ProdutoForm(ModelForm):
	nome		= forms.CharField()
	slug		= forms.CharField()
	categoria	= forms.ModelChoiceField(queryset=Categoria.objects.all())
	tipo		= forms.ModelChoiceField(queryset=Tipo.objects.all())
	cor 		= forms.ModelMultipleChoiceField(queryset=Cor.objects.all())
	tamanho 	= forms.ModelMultipleChoiceField(queryset=Tamanho.objects.all())
	descricao  	= forms.CharField()
	detalhe    	= forms.CharField()
	preco      	= forms.FloatField()
	
	model = Produto