from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
	url(r'^$', dashboard, name='dashboard'),   
    url(r'^entrar/$', views.login, 
    	{'template_name':'accounts/login.html'}, name='login'),  
	url(r'^SAIR/$', views.logout, 
    	{'next_page':'index'}, name='logout'),   
    url(r'^registrar/$', register, name='register'), 
    url(r'^dados_cadastrais/$', profile, name='profile'),  
    url(r'^enderecos/$', address, name='address'),
    url(r'^enderecos/(?P<id>\d+)/$', delete_address, name='delete_address'),
]