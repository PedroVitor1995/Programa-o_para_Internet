from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
	return render(request, 'index.html')

def exibir(request, question_id):
	
	question = Question()
	
	if question_id == 1:
		question = Question('Qual seu nome?','06-04-2019')

	if question_id == 2:
		question = Question('Qual seu sexo?','06-04-2019')

	if question_id == 3:
		question = Question('Qual sua data de nascimento?','06-04-2019')


	return render(request, 'question.html', {'question' : question})