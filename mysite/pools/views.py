from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404

from .models import Questao,Opcao


# Create your views here.

def index(request):
	questao_lista = Questao.objects.order_by('-data_pub')
	saida = {'questao_lista':questao_lista}
	return render(request,'index.html',saida)

def detalhe(request,questao_id):
	try:
		questao = Questao.objects.get(pk=questao_id)
	except Questao.DoesNotExist:
		raise Http404("Questao não existe")
	return render(request,'detalhe.html',{'questao':questao})

def votacao(request,questao_id):
	questao = get_object_or_404(Questao,pk=questao_id)
	try:
		seleciona_opcao = questao.opcao_set.get(pk=request.POST['opcao'])
	except (KeyError,Opcao.DoesNotExist):
		return render(request,'detalhe.html',{'questao':questao,'error_message':"Nenhuma opção foi selecionada"})
	else:
		seleciona_opcao.votos += 1
		seleciona_opcao.save()
		return render(request,'votacao.html',{'questao':questao})

def resultado(request,questao_id):
	total_votos = 0

	questao = get_object_or_404(Questao,pk=questao_id)

	for opcao in questao.opcao_set.all():
		total_votos += opcao.votos

	return render(request,'resultado.html',{'questao':questao,'total_votos':total_votos})

def manage(request, questao_id):
	questao = Questao.objects.get(id=questao_id)
	return render(request, 'manage.html', {'questao':questao})

