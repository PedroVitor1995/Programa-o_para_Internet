from django.urls import path
from perfis import views

urlpatterns = [
	path('', views.timeline, name='timeline'),
	path('index/', views.index, name='index'),
    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/', views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/', views.desfazer, name='desfazer'),
    path('perfil/<int:perfil_id>/bloquear/',views.bloquear, name='bloquear'),
    path('perfil/<int:perfil_id>/desbloquear/', views.desbloquear, name='desbloquear'),
    path('perfil/<int:perfil_id>/melhores_amigos/', views.adicionar_melhor_amigo, name='melhores_amigos'),
    path('perfil/<int:perfil_id>/remover_melhor_amigo/', views.remover_melhor_amigo, name='remover_melhor_amigo'),
    path('lista_melhores_amigos/', views.listar_melhores_amigos, name='exibir_melhores_amigos'),
    path('desativar_perfil/', views.desativar_perfil, name='desativar_perfil'),
    path('convite/<int:convite_id>/aceitar/', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar/', views.recusar, name='recusar'),
    path('alterar_senha/',views.alterar_senha,name='alterar_senha'),
    path('pesquisar_usuario/',views.pesquisar_usuario,name='pesquisar_usuario'),
    path('postar/', views.postar, name='postar'),
    path('postagem/excluir/<int:postagem_id>/', views.excluir_postagem, name='excluir_postagem'),
    path('postagem/<int:post_id>/curtir/', views.curtir, name='curtir'),
    path('postagem/<int:post_id>/descurtir',  views.descurtir, name='descurtir')
]