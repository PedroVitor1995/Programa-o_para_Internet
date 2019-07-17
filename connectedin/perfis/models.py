from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
	telefone = models.CharField(max_length=11, null=False)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User,related_name="perfil",on_delete=models.CASCADE)
	ativa = models.BooleanField(default=True)
	justificativa = models.TextField(null=True)
	contatos_bloqueados = models.BooleanField(default=False)


	@property
	def nome(self):
		return self.usuario.username
		
	@property
	def email(self):
		return self.usuario.email

	@property
	def superuser(self):
		return self.usuario.is_superuser

	@property
	def get_postagens(self):
		return Postagem.objects.filter(id=self.id)

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

<<<<<<< HEAD
=======
	def bloquear(self, perfil_a_bloquear):
		self.contatos_bloqueados.add(perfil_a_bloquear)

	def compartilhar(self, postagem_id):
		minhas_postagems = Postagem.objects.filter(id=self.id).all()
		postagem = Postagem.objects.get(id=postagem_id)
		minhas_postagems.append(postagem) #não tenho certeza se é assim

>>>>>>> eb8ab2b85d20b1d5fa04c7258dfb7922f5545dd1
class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE , related_name='convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()
		
	def recusar(self):
		self.delete()

class Postagem(models.Model):
	texto_postagem = models.CharField(max_length=300)
	data_postagem = models.DateTimeField(auto_now_add=True)
	perfil = models.ForeignKey(Perfil, related_name='usuario_postagem', on_delete=models.CASCADE)


	@property
	def curtidas(self):
		lista_curtidas = []
		for like in self.curtidas.all():
			lista_curtidas.append(like.perfil.id)

		return lista_curtidas

	@property
	def total_curtidas(self):
		curtidas = Curtida.objects.filter(post=self).exists()
		
		if curtidas:
			return Curtida.objects.filter(post=self).count
		return 0

	def __str__(self):
		return self.texto_postagem

	def excluir(self):
		self.delete()

class Curtida(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='curti')
	post = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='curtidas')

	def descurtir(self):
		self.delete()