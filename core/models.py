from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontosTuristico(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracao)
	comentarios = models.ManyToManyField(Comentario)
	avaliacoes = models.ManyToManyField(Avaliacao)
	endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
	foto = models.ImageField(upload_to="pontos_turisticos", null=True, blank=True)

	@property
	def descricao_completa2(self):
		return '%s - %s' % (self.nome, self.descricao)

	def __str__(self) -> str:
		return self.nome
