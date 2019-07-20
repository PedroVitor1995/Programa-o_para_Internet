from django.views import View
from perfis.models import *
from perfis.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator, InvalidPage

# Create your views here.

#Timeline
@login_required
def timeline(request):
	posts = Postagem.objects.all()

	return render(request,'home.html',{'perfis': Perfil.objects.all(),\
                   'perfil_logado' : get_perfil_logado(request),\
                   'posts':posts})

@login_required
@transaction.atomic
def index(request):
	return render(request, 'index.html',{'perfis': Perfil.objects.all(),\
                   'perfil_logado' : get_perfil_logado(request)})

@login_required
@transaction.atomic
def exibir_perfil(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	ja_eh_contato = perfil in perfil_logado.contatos.all()

	if perfil_logado.ativa == False:
		return render(request,'status.html', {'perfil_logado': perfil_logado})

	return render(request, 'perfil.html',{'perfil' : perfil,
                   'perfil_logado' : get_perfil_logado(request),
                   'ja_eh_contato':ja_eh_contato})

@login_required
@transaction.atomic
def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	if perfil_logado.pode_convidar(perfil_a_convidar):
		perfil_logado.convidar(perfil_a_convidar)

	return redirect('index')


@login_required
def get_perfil_logado(request):
	return request.user.perfil

@login_required
@transaction.atomic
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

#Rejeitar solicitação
@login_required
@transaction.atomic
def recusar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.recusar()
	return redirect('index')

#Desfazer amizade
@login_required
@transaction.atomic
def desfazer(request,perfil_id):
	perfil_a_desfazer = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.desfazer(perfil_a_desfazer)
	return redirect('index')
	 	
#Alterar senha
@login_required
@transaction.atomic
def alterar_senha(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Sua senha foi atualizada com sucesso.')
			return redirect('alterar_senha')
		else:
			senha_exists = User.objects.filter(password=request.POST['old_password']).exists()
			if senha_exists:
				messages.error(request,'A senha atual não confere.')

			elif request.POST['new_password2'] != request.POST['new_password1']:
				messages.error(request, 'A confirmação da senha não confere com a nova senha.')
			else:
				messages.error(request, 'Verifique seus dados.')

			

	else:
		form = PasswordChangeForm(request.user)

	return render(request, 'alterar_senha.html', {'perfil_logado' : get_perfil_logado(request),'form': form})

#Bloquear usuário
@login_required
@transaction.atomic
def bloquear(request, perfil_id):
	perfil = get_perfil_logado(request)
	perfil_a_bloquear = Perfil.objects.get(id=perfil_id)
	if perfil != perfil_a_bloquear :
		perfil.contatos_bloqueados.add(perfil_a_bloquear)
		messages.success(request,'Perfil foi bloqueado.')
	else:
		messages.error(request, 'O usuário não pode se bloquear.')

	return redirect('bloquear')


#Pesquisar usuário
@login_required
@transaction.atomic
def pesquisar_usuario(request):
	perfil_logado = get_perfil_logado(request)
	nome_buscado = request.GET['nome']
	if nome_buscado:
		resultado = Perfil.objects.filter(nome__contains=nome_buscado) \
							.exclude(nome=perfil_logado.nome) \
							.exclude(bloqueado=True) \
							.exclude(ativo=False)
		contexto = {
			"perfil": perfil_logado,
			"resultado": resultado,
			"nome_buscado": nome_buscado
			}
		return render(request, 'busca.html', contexto)

	contexto = {
		"perfil": perfil_logado,
		"resultado": resultado,
		"nome_buscado": nome_buscado
		}
	return render(request, 'busca.html', contexto)


def tornar_superusuario(request,  perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil.usuario.is_superuser = True
	perfil.usuario.save()
	perfil.save()
	messages.success(request, 'Este perfil agora é super usuario')
	return redirect('index')


@login_required
def curtir(request, post_id):
	postagem = Postagem.objects.get(id=post_id)
	curtida = Curtida(perfil=get_perfil_logado(request), post=postagem)
	curtida.save()
	return redirect('index')

@login_required
def descurtir(request, post_id):
	postagem = Postagem.objects.get(id=post_id)
	curtida = Curtida(perfil=get_perfil_logado(request), post=postagem)
	curtida.descurtir()
	return redirect('index')


@login_required
def postar(request):
	if request.POST:
		postagem = Postagem()
		postagem.perfil = get_perfil_logado(request)
		form = PostagemForm(request.POST, request.FILES)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()       
			messages.success(request, 'Postagem feita com sucesso.')
		else:
			messages.error(request, 'Não foi possivel fazer a postagem')

	return redirect('timeline')

@login_required
def excluir_postagem(request, postagem_id):
	post = Postagem.objects.get(id=postagem_id)
	if post.perfil == get_perfil_logado(request) or get_perfil_logado(request).usuario.is_superuser:
		post.delete()
		messages.success(request, 'A postagem foi excluida.')
	else:
		messages.error(request, 'Você não pode excluir a postagem')

	return redirect('timeline')


