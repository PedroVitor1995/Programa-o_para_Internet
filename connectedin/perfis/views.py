from perfis.models import Perfil, Convite
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
	return render(request, 'index.html',{'perfis': Perfil.objects.all(),
                   'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir_perfil(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html',{'perfil' : perfil,
                   'perfil_logado' : get_perfil_logado(request),
                   'ja_eh_contato':ja_eh_contato})

@login_required
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.perfil

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

#Rejeitar solicitação
@login_required
def recusar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.recusar()

	return redirect('index')

#Desfazer amizade
@login_required
def desfazer(request,perfil_id):
	perfil_a_desfazer = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.desfazer(perfil_a_desfazer)
	return redirect('index')
	 	
@login_required
#Alterar senha:
def alterar_senha(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Sua senha foi atualizada com sucesso!')
			return redirect('senha')
		else:
			messages.error(request, 'Não foi possível atualizar senha')
	else:
		form = PasswordChangeForm(request.user)
	
	return render(request, 'alterar_senha.html', {'perfil_logado' : get_perfil_logado(request),'form': form})
