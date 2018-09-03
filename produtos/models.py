from django.db import models
from unicodedata import normalize
from django.utils import timezone

class Produto (models.Model):

	codigo		= models.AutoField('Código', primary_key=True)
	referencia	= models.CharField('Referência', unique=True, max_length=30, blank=True, null=True)
	nome		= models.CharField('Nome', max_length=100, blank=False, null=False)
	slug		= models.SlugField(max_length=150, blank=True, null=True)
	categoria	= models.ForeignKey('Categoria', on_delete=models.CASCADE)
	tipo		= models.ForeignKey('Tipo', on_delete=models.CASCADE)
	cor 		= models.ManyToManyField('Cor')
	tamanho 	= models.ManyToManyField('Tamanho')
	descricao  	= models.TextField('Descrição', blank=True)
	detalhe    	= models.CharField(max_length=50, blank=True, null=True)
	preco      	= models.FloatField('Preço', blank=False, null=False)
	#preco      	= models.DecimalField('Preço', blank=False, null=False, max_digits=6, decimal_places=2)
	#foto 		= models.ImageField(upload_to = "img",blank=True)
	disponivel	= models.BooleanField('Disponível', default=True)

	@models.permalink
	def get_absolute_url(self):
		return('produto', (), {'slug':self.slug})

	def __fotos__(self):
		return FotoProduto.objects.filter(cod_produto=self.codigo)
	fotos = __fotos__

	def __str__(self):
		return (self.tipo.nome + " " + self.nome)

	class Meta:
		ordering = ['tipo','nome']

	def save(self):
		if self.codigo:
			i = 3-len(str(self.codigo))
			cod = str(self.codigo)
			while(i<=3):
				cod = "0" + cod
				i+=1
			self.referencia = (str(self.tipo)[0] + str(self.tipo)[1] + cod).upper()
		else:
			p = Produto.objects.latest('codigo')
			cod = str(p.codigo+1)
			i = 3-len(cod)
			while(i<=3):
				cod = "0" + cod
				i+=1
			self.referencia = (str(self.tipo)[0] + str(self.tipo)[1] + cod).upper()
		super(Produto, self).save()

class Categoria (models.Model):

	codigo		= models.AutoField(primary_key=True)
	nome		= models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.nome 

	class Meta:
		ordering = ['nome']

class Tipo (models.Model):
	
	codigo		= models.AutoField(primary_key=True)
	nome		= models.CharField(max_length=50, blank=False, null=False)
	categoria 	= models.ManyToManyField('Categoria', db_table='produtos_tipo_categoria')

	def __str__(self):
		return self.nome 

	class Meta:
		ordering = ['nome']

class Tamanho (models.Model):
	
	codigo		= models.AutoField(primary_key=True)
	nome		= models.CharField(max_length=50, blank=False, null=False)
	tipo 		= models.ManyToManyField('Tipo')

	def __str__(self):
		return self.nome 

	class Meta:
		ordering = ['nome']

class Cor (models.Model):
	
	codigo		= models.AutoField(primary_key=True)
	nome		= models.CharField(max_length=50, blank=False, null=False)
	tipo 		= models.ManyToManyField('Tipo')

	def __str__(self):
		return self.nome 

	class Meta:
		verbose_name = u'cor'
		verbose_name_plural = u'cores'
		ordering = ['nome']

class FotoProduto (models.Model):

	codigo		= models.AutoField(primary_key=True)
	cod_produto	= models.ForeignKey('Produto', on_delete=models.CASCADE)
	foto 		= models.ImageField(upload_to = "img",blank=True)

	def __str__(self):
		return (self.cod_produto.tipo.nome + " " + self.cod_produto.nome)
class Meta:
	ordering = ['nome']