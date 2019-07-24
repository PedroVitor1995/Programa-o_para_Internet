from django.forms import ModelForm
from meuapp.models import *

class PessoaForm(ModelForm):
	class Meta:
		model = Pessoa
		fields = ['nome']
		
class TarefaForm(ModelForm):
	class Meta:
		model = Tarefa
		fields = '__all__'
