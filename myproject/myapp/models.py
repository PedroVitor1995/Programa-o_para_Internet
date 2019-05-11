from django.db import models

# Create your models here.

# Exercicio 1
class Pessoa(models.Model):
	TAM_ROUPA = (
		('P','Pequena'),
		('M','Media'),
		('G','Grande'),
	)
	primeiro_nome = models.CharField(max_length=30)
	segundo_nome = models.CharField(max_length=30)
	data_pub = models.DateField()
	tam_roupa = models.CharField(max_length=1, choices=TAM_ROUPA, null=True)

# Exercicio 2
class Fruta(models.Model):
	nome = models.CharField(max_length=50, primary_key=True)

# Exercicio 3
class Fabricante(models.Model):
	nome = models.CharField(max_length=50)

class Carro(models.Model):
	nome = models.CharField(max_length=50)
	fabricante = models.ForeignKey(Fabricante,on_delete=models.CASCADE,related_name='carros')

# Exercicio 4
class Cobertura(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Pizza(models.Model):
	nome = models.CharField(max_length=50)
	coberturas = models.ManyToManyField(Cobertura)

	def __str__(self):
		return self.nome

# Exercicio 5
class CPF(models.Model):
	numero = models.CharField(max_length=9)

	def calcular_dv(self):
		return '00'

	def __str__(self):
		return self.numero + '-' + self.calcular_dv()

class PessoaFisica(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.OneToOneField(CPF,related_name='pessoa_fisica',on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

# Exercicio 6
class Pessoa1(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Grupo(models.Model):
	nome = models.CharField(max_length=50)
	membros = models.ManyToManyField(Pessoa1,through='Membroship')

	def __str__(self):
		return self.nome

class Membroship(models.Model):
	pessoa = models.ForeignKey(Pessoa1,on_delete=models.CASCADE)
	grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
	data_entrada = models.DateField()
	motivo_convite = models.CharField(max_length=50)

# Exercicio 7
class Blog(models.Model):
	nome = models.CharField(max_length=50)

class Entry(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.CharField(max_length=500)
	data_pub = models.DateTimeField()
	blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

# Exercicio 8
class Usuario(models.Model):
	email = models.CharField(max_length=50)
	senha = models.CharField(max_length=50)
	dt_nasc = models.DateField()

class Perfil(models.Model):
	nome = models.CharField(max_length=100)
	usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='perfis')
	contatos = models.ManyToManyField('self')	

class Postagem(models.Model):
	texto = models.CharField(max_length=250)
	data = models.DateField()
	perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='postagens') 

class Comentario(models.Model):
	texto = models.CharField(max_length=200)
	data = models.DateField()
	perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='comentarios') 
	postagem = models.ForeignKey(Postagem,on_delete=models.CASCADE,related_name='comentarios')

class Reacao(models.Model):
	TIPO_REACAO = (
		('Curtir','Curtiu'),
		('Amar','Amou'),
		('Rir','Riu'),
		('Impressionar','Se impressionou'),
		('Triste','Ficou triste'),
		('Irritar','Se irritou'),
	)
	tipo = models.CharField(max_length=50,choices=TIPO_REACAO)
	postagem = models.ForeignKey(Postagem,on_delete=models.CASCADE)
	perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE) 
	data = models.DateField()
	peso = models.IntegerField()