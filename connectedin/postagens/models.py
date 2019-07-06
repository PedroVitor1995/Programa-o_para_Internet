from django.db import models
from perfis.models import *

# Create your models here.

class Postagem(model.Model):
	texto_postagem = models.CharField(max_length=300)
	data_postagem = models.DateTimeField(auto_now_add=True)
	perfil = models.ForeignKey(Perfil, related_name='usuario_postagem', on_delete=models.CASCADE)

	class Meta:
		ordering = ['-data']

	def __str__(self):
		return self.texto_postagem

	