from django.urls import path
from meuapp import views

urlpatterns = [
	path('',views.listar_tarefas, name='listar_tarefas'),
    path('adicionar_tarefa/', views.criar_tarefa, name='adicionar_tarefa'),
    path('tarefa/<int:tarefa_id>/', views.finalizar_tarefa, name='finalizar_tarefa'),
] 