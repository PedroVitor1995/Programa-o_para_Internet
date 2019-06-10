from django.db import models

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=100)
	texto = models.CharField(max_length=255)

	def __str__(self):
		return self.titulo

class Reporter(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Article(models.Model):
	data_pub = models.DateTimeField('data publicacao')
	titulo = models.CharField(max_length=200)
	contexto = models.TextField()
	reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo

class Autor(models.Model):
	TITULO_CHOICES = (
		('MR','Mr.'),
		('MRS','Mrs.'),
		('MS','Ms.'),	
	)
	nome = models.CharField(max_length=100)
	titulo = models.CharField(max_length=3,choices=TITULO_CHOICES)
	birth_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.nome

class Book(models.Model):
	nome = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor)

	def __str__(self):
		return self.nome