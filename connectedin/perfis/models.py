from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	telefone = models.CharField(max_length=11, null=False)
	nome_empresa = models.CharField(max_length=60, null=False)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User,related_name="perfil",on_delete=models.CASCADE)

	@property
	def nome(self):
		return self.usuario.username
		
	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		Convite(solicitante=self, convidado=perfil_convidado).save()

	def desfazer(self, perfil_id):
		self.contatos.remove(perfil_id)
		self.save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE , related_name='convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()
		
	def recusar(self):
		self.delete()