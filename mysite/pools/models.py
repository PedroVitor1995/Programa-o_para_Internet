import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Questao(models.Model):
	texto_questao = models.CharField(max_length=200)
	fechada = models.BooleanField(default=False)
	data_pub = models.DateField('data publicada')

	def __str__(self):
		return self.texto_questao

	def alterar_status(self):
		if self.fechada:
			self.fechada = False
		else:
			self.fechada = True

		self.save()

	def adicionar_opcao(self,opcao):
		opcao.questao = self
		opcao.save()

class Opcao(models.Model):
	questao = models.ForeignKey(Questao,on_delete=models.CASCADE,related_name='opcoes')
	texto_opcao = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.texto_opcao

	def deletar(self,id_opcao):
		self.questao = None
		self.votos.delete()
		self.save()
		