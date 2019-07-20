from django.urls import path
from perfis import views

urlpatterns = [
	path('', views.timeline, name='timeline'),
	path('index/', views.index, name='index'),
    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/', views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/', views.desfazer, name='desfazer'),
    path('perfil/<int:perfil_id>/bloqueiar/',views.bloquear, name='bloquear'),
    path('convite/<int:convite_id>/aceitar/', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar/', views.recusar, name='recusar'),
    path('alterar_senha/',views.alterar_senha,name='alterar_senha'),
    path('pesquisar_usuario/',views.pesquisar_usuario,name='pesquisar_usuario'),
    path('postar/', views.postar, name='postar'),
    path('postagem/excluir/<int:postagem_id>/', views.excluir_postagem, name='excluir_postagem'),
]