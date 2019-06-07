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

class Opcao(models.Model):
	questao = models.ForeignKey(Questao,on_delete=models.CASCADE)
	texto_opcao = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.texto_opcao