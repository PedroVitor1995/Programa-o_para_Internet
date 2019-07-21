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
		mensagem = 'Você enviou um convite para {} .'.format(perfil_a_convidar.nome)
		messages.success(request,mensagem)

	return redirect('index')


@login_required
def get_perfil_logado(request):
	return request.user.perfil

@login_required
@transaction.atomic
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('timeline')

#Rejeitar solicitação
@login_required
@transaction.atomic
def recusar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.recusar()
	return redirect('timeline')

#Desfazer amizade
@login_required
@transaction.atomic
def desfazer(request,perfil_id):
	perfil_a_desfazer = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.desfazer(perfil_a_desfazer)
	return redirect('timeline')

	mensagem = 'O contato com o perfil {} foi desfeito.'.format(perfil_a_desfazer.nome)
	messages.success(request,mensagem)

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
		mensagem = 'O perfil {} foi bloqueado.'.format(perfil_a_bloquear.nome)
		messages.success(request,mensagem)
	else:
		messages.error(request, 'O usuário não pode se bloquear.')

	return render(request, 'index.html',{'perfis': Perfil.objects.all(),\
										'perfil' : perfil,\
                   						'perfil_logado' : get_perfil_logado(request)})

# Desbloquear usuário
@login_required
def desbloquear(request, perfil_id):
    perfil_desbloquear = Perfil.objects.get(id=perfil_id)
    get_perfil_logado(request).contatos_bloqueados.remove(perfil_desbloquear)

    mensagem = 'O perfil {}  foi desbloqueado.'.format(perfil_desbloquear.nome)
    messages.success(request, mensagem)

    return render(request, 'index.html',{'perfis': Perfil.objects.all(),\
    									'perfil_logado' : get_perfil_logado(request)})

#Pesquisar usuário
@login_required
@transaction.atomic
def pesquisar_usuario(request):
	nome = request.GET['nome']
	perfis_econtrados = Perfil.objects.filter(nome__startswith=nome)

	paginator = Paginator(perfis_econtrados, 10)
	page = request.GET.get('page')
	task = paginator.get_page(page)

	contexto = {
		'perfis_econtrados': task,
		'perfil_logado': get_perfil_logado(request),
		'range_paginator': range(1, task.paginator.num_pages + 1),
		'current_page': int(page) if page else 1
	}
	return render(request, 'busca.html', contexto)

@login_required
def tornar_super_usuario(request,  perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil.usuario.is_superuser = True
	perfil.usuario.save()
	perfil.save()
	messages.success(request, 'Este perfil agora é super usuario')
	return redirect('index')

@login_required
def tirar_superusuario(request, perfil_id):
	if not get_perfil_logado(request).usuario.is_superuser:
		msg = "Acesso negado"
		messages.error(request, msg)
		return redirect('index')

	perfil = Perfil.objects.get(id=perfil_id).usuario
	perfil.is_superuser = False
	perfil.save()

	msg_sucess = "Super usuário retirado deste perfil"
	messages.success(request, msg_sucess)
	return redirect('index')

@login_required
def curtir(request, post_id):
	postagem = Postagem.objects.get(id=post_id)
	curtida = Curtida(perfil=get_perfil_logado(request), post=postagem)
	curtida.save()
	return redirect('timeline')

@login_required
def descurtir(request, post_id):
	postagem = Postagem.objects.get(id=post_id)
	curtida = Curtida(perfil=get_perfil_logado(request), post=postagem)
	curtida.descurtir()
	return redirect('timeline')


@login_required
def postar(request):
	if request.POST:
		perfil = get_perfil_logado(request)
		form = PostagemForm(request.POST, request.FILES)
		if form.is_valid():
			texto = request.POST['texto']
			Postagem.objects.create(texto_postagem = texto, perfil = perfil)
			messages.success(request, 'Postagem feita com sucesso.')
		else:
			messages.error(request, 'Não foi possivel fazer a postagem')

	return redirect('timeline')

@login_required
def excluir_postagem(request, postagem_id):
	post = Postagem.objects.get(id=postagem_id)
	message = ''
	if post.perfil == get_perfil_logado(request) or get_perfil_logado(request).usuario.is_superuser:
		post.delete()
		message = 'A postagem foi excluida com sucesso.'
	else:
		message = 'Não foi possivel excluir postagem.'

	return render(request, 'home.html', {'message':message,'perfil_logado' : get_perfil_logado(request)})

# Desativar perfil
@login_required
def desativar_perfil(request):
    perfil_logado = get_perfil_logado(request)
    perfil_logado.ativo = False
    perfil_logado.save()
    messages.info(request, 'Perfil desativo. Aguardamos o seu retorno!')

    return redirect('login')

# Ativar perfil
@login_required
def ativar_perfil(request):
    if request.POST:
        print(request.POST.keys())
        if not 'reativar' in request.POST.keys():
            logout(request)
            return redirect('login')

        perfil_logado = get_perfil_logado(request)
        perfil_logado.ativo = True
        perfil_logado.save()

        mensagem = 'Perfil reativado com sucesso. Seja bem-vindo novamente, {}!'.format(perfil_logado)
        messages.success(request, mensagem)
        return redirect('index')

    return render(request, 'reativar_perfil.html', {'perfil_logado': get_perfil_logado(request)})


# Adicionar aos melhores amigos
@login_required
def adicionar_melhor_amigo(request,perfil_id):
	perfil = get_perfil_logado(request)
	perfil_a_melhor_amigo = Perfil.objects.get(id=perfil_id)
	if perfil != perfil_a_melhor_amigo :
		perfil.melhores_amigos.add(perfil_a_melhor_amigo)
		mensagem = 'O perfil {} foi adicionado a lista de melhores amigos.'.format(perfil_a_melhor_amigo.nome)
		messages.success(request,mensagem)

	return render(request, 'index.html',{'perfis': Perfil.objects.all(),\
										'perfil' : perfil,\
                   						'perfil_logado' : get_perfil_logado(request)})


# Listar de melhores amigos
@login_required
def listar_melhores_amigos(request):
	perfil_logado = get_perfil_logado(request)
	melhores_amigos = perfil_logado.melhores_amigos.all()

	return render(request, 'melhores_amigos.html',{'perfil_logado' : get_perfil_logado(request),
                   'melhores_amigos':melhores_amigos})


# Remover da listar de melhores amigos
@login_required
def remover_melhor_amigo(request,perfil_id):
	perfil_logado = get_perfil_logado(request)
	perfil_a_remover = Perfil.objects.get(id=perfil_id) 

	if perfil_logado != perfil_a_remover:
		perfil_logado.melhores_amigos.remove(perfil_a_remover)
		mensagem = 'O perfil {} foi removido a lista de melhores amigos.'.format(perfil_a_remover.nome)
		messages.success(request,mensagem)

	return render(request, 'melhores_amigos.html',{'perfis': Perfil.objects.all(),\
                   						'perfil_logado' : get_perfil_logado(request)})

