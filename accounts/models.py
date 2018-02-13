from django.db import models
from django.contrib.auth.models import User

class UserAddress (models.Model):

	codigo		= models.AutoField('Código', primary_key=True)
	user 		= models.ForeignKey(User, related_name='address', on_delete=models.CASCADE)
	logradouro	= models.CharField('Logradouro', max_length=255, blank=False, null=False)
	numero		= models.CharField('Numero', max_length=10, blank=False, null=False)
	complemento	= models.CharField('Complemento', max_length=255, blank=True, null=True)
	pontoref	= models.CharField('Ponto de referência', max_length=255, blank=True, null=True)
	bairro		= models.CharField('Bairro', max_length=70, blank=False, null=False)
	cidade		= models.CharField('Cidade', max_length=70, blank=False, null=False)
	estado		= models.CharField('UF', max_length=2, blank=False, null=False)
	cep			= models.CharField('CEP', max_length=10, blank=False, null=False)

class UserComplements (models.Model):

	user 		= models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	cpf			= models.CharField('CPF', max_length=11, blank=False, null=False)
	celular		= models.CharField('Celular', max_length=11, blank=False, null=False)
	data_nasc	= models.DateField()
	sexo 		= models.CharField('Sexo', max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino')))