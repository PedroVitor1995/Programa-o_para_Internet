from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfis.models import *
from usuarios.forms import RegistrarUsuarioForm
from django.contrib import messages

# Create your views here.

class RegistrarUsuarioView(View):
	template_name = 'registrar.html'

	def get(self,request):
		return render(request,self.template_name)

	def post(self,request):
		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():
			dados_form = form.cleaned_data

			email_exists = User.objects.filter(email=request.POST['email']).exists()

			if email_exists:
				messages.success(request,'Email já existente.')
				return render(request,self.template_name,{'form':form})

			usuario = User.objects.create_user(username = dados_form['nome'],
												email = dados_form['email'],
												password = dados_form['senha'])
			perfil = Perfil(telefone = dados_form['telefone'],
							nome_empresa = dados_form['nome_empresa'],
							usuario = usuario)

			perfil.save()

			messages.success(request,'Cadastro realizado com sucesso')

			return redirect('registrar')

		else:
			if request.POST['senha_confirmar'] != request.POST['senha']:
				messages.error(request, 'A confirmação da senha não confere com a nova senha.')


		return render(request,self.template_name,{'form':form})


#Recuperar senha
def redefinir_senha(request):
	pass
