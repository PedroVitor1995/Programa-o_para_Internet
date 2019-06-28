from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/', views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/', views.desfazer, name='desfazer'),
    path('convite/<int:convite_id>/aceitar/', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar/', views.recusar, name='recusar'),
    path('alterar_senha/',views.alterar_senha,name='alterar_senha'),
]