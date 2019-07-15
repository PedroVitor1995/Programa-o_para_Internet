from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	telefone = models.CharField(max_length=11, null=False)
	nome_empresa = models.CharField(max_length=60, null=False)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User,related_name="perfil",on_delete=models.CASCADE)
	bloqueado = models.BooleanField(default=False)
	ativo = models.BooleanField(default=True)

	@property
	def nome(self):
		return self.usuario.username
		
	@property
	def email(self):
		return self.usuario.email

	def desfazer(self, perfil_id):
		self.contatos.remove(perfil_id)
		self.save()

	def convidar_a_si_mesmo(self, perfil):
		return self == perfil

	def e_contato(self, perfil):
		return self.contatos.filter(id=perfil.id).exists()

	def possui_convite(self, perfil):
		return (Convite.objects.filter(solicitante=self, convidado=perfil).exists() or
				Convite.objects.filter(solicitante=perfil, convidado=self).exists())

	def pode_convidar(self, perfil):
		nao_pode = self.convidar_a_si_mesmo(perfil) or self.e_contato(perfil) or self.possui_convite(perfil)
		return not nao_pode

	def convidar(self, perfil_convidado):
		if self.pode_convidar(perfil_convidado):
			Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE , related_name='convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()
		
	def recusar(self):
		self.delete()