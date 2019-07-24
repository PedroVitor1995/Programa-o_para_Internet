from django.db import models

# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=15)

class Tarefa(models.Model):
	descricao = models.CharField(max_length=200)
	concluida = models.BooleanField(default=False)
	pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE, related_name='pessoa')
