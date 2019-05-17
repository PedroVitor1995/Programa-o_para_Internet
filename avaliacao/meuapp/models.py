from django.db import models

# Create your models here.

class Processo(models.Model):
	DESCRICAO =(
		('S','Sigiloso'),
		('N','Normal'),
		('A','Administrativo')
	)
	numero = models.CharField(max_length=25)
	texto = models.CharField(max_length=250)
	tipo = models.CharField(max_length=1,choices=DESCRICAO) 
	ativo = models.BooleanField()

class Apensamento(models.Model):
	processo_original = models.ForeignKey(Processo,on_delete=models.CASCADE)
	data_apensamento = models.DateField(auto_now_add=True)

class Interessado(models.Model):
	nome = models.CharField(max_length=100)
	data_nascimento = models.DateField(auto_now_add=True)
	cpf = models.CharField(max_length=15)
	processo = models.ManyToManyField(Processo)
	advogado = models.ForeignKey('Advogado',on_delete=models.CASCADE)

class Advogado(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=15)
	registro = models.OneToOneField('Registro',on_delete=models.CASCADE,related_name='advogados')

class Registro(models.Model):
	matricula = models.CharField(max_length=20)
	data_validade = models.DateField(auto_now_add=True)