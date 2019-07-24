from django.shortcuts import render,redirect
from .forms import *
from .models import *

def criar_tarefa(request):
	if request.method == 'POST':
		form = TarefaForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('listar_tarefas')
	else:
		form = TarefaForm()
		return render(request,'tarefas.html',{'form':form})

def listar_tarefas(request):
	tarefas = Tarefa.objects.all()
	return render(request,'listar_tarefas.html',{'tarefas':tarefas})

def finalizar_tarefa(request, tarefa_id):
	tarefa = Tarefa.objects.get(id=tarefa_id)
	tarefa.concluida = True
	tarefa.save()
	return redirect('listar_tarefas')

