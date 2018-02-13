from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import RegisterForm, AddressForm
from .models import UserAddress, UserComplements
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def dashboard(request):
	template_name = 'accounts/dashboard.html'
	context = {
	}
	return render(request, template_name, context)

def register(request):
	template_name = 'accounts/register.html'
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = RegisterForm()
	context = {
		'form': form
	}

	return render(request, template_name, context)

@login_required
def profile(request):
	template_name = 'accounts/profile.html'

	if request.method == 'POST':
		user = User.objects.get(username=request.POST.get('user'))
		user.profile.cpf = (request.POST.get('cpf').replace(".","").replace("-",""))
		user.profile.celular = request.POST.get('celular').replace("(","").replace(")","").replace("-","")
		user.profile.data_nasc = request.POST.get('data_nasc')
		user.profile.sexo = request.POST.get('genero')
		user.profile.save()
		print (user.profile.cpf, request.POST.get('cpf').replace(".","").replace("-",""))
		print (request.POST.get('celular'))
		print (request.POST.get('data_nasc'))
		print (request.POST.get('genero'))

	return render(request, template_name)

@login_required
def address(request):
	template_name = 'accounts/address.html'

	if request.method == 'POST':
		if 'id' in request.POST and request.POST.get('id')!='':
			endereco = UserAddress.objects.get(codigo=request.POST.get('id'))
			endereco.logradouro = request.POST.get('logradouro')
			endereco.numero = request.POST.get('numero')
			endereco.complemento = request.POST.get('complemento')
			endereco.pontoref = request.POST.get('pontoref')
			endereco.bairro = request.POST.get('bairro')
			endereco.cidade = request.POST.get('cidade')
			endereco.estado = request.POST.get('estado')
			endereco.cep = request.POST.get('cep')
			endereco.save()
		else:
			endereco = UserAddress()
			endereco.user = User.objects.get(username=request.POST.get('user'))
			endereco.logradouro = request.POST.get('logradouro')
			endereco.numero = request.POST.get('numero')
			endereco.complemento = request.POST.get('complemento')
			endereco.pontoref = request.POST.get('pontoref')
			endereco.bairro = request.POST.get('bairro')
			endereco.cidade = request.POST.get('cidade')
			endereco.estado = request.POST.get('estado')
			endereco.cep = request.POST.get('cep')
			endereco.save()

	print (request.user.address.all(), request.user.pk)
	context = {
		'value': 'value',
	}
	return render(request, template_name, context)

@login_required
def delete_address(request, id):
	template_name = 'accounts/address.html'
	UserAddress.objects.get(codigo=id).delete()
	return render(request, template_name)

