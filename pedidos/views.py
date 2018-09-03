from django.shortcuts import render, redirect
from pagseguro.api import PagSeguroItem, PagSeguroApi
from madamechique import settings
from decimal import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def pagamento(request):
	carrinho = request.session.get('carrinho')
	print(carrinho)
	#user = User.objects.get(username=request.POST.get('user'))
	user = request.user
	useradress = user.address.all().first()
	pagseguro_api = PagSeguroApi(reference=settings.PAGSEGURO_REFERENCE,
								#extraAmount=extra_amount,
								senderEmail=user.email,
								senderName=user.first_name +' '+ user.last_name,
								senderAreaCode='83',
								senderPhone='988766704',
								postalCode=useradress.cep
								)

	for produto in carrinho:
		print(Decimal(str(produto.get('preco'))).quantize(Decimal('1.00'), rounding=ROUND_DOWN))
		
		item = PagSeguroItem(
								id=produto.get('ref'),
								description = produto.get('produto'),
								amount = Decimal(str(produto.get('preco'))).quantize(Decimal('1.00'), rounding=ROUND_DOWN),
								quantity = produto.get('quantidade'),
								shipping_cost = '25.00',
								weight = 500
							)
		pagseguro_api.add_item(item)
		
	data = pagseguro_api.checkout()
	
	return redirect(data['redirect_url'])

