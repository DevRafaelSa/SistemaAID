from django.db import models
from cadastros.models import Parceiro
from usuarios.models import User
# Create your models here.

class FrequenciaAluno(models.Model):
    """Registro de Frequência do aluno"""
    nome = models.CharField(max_length=100, blank=True, null=True)
    dia = models.DateField(verbose_name='Data do registro', auto_now_add=True)
    entrada = models.TimeField(verbose_name='Entrada', blank=True, null=True)
    saida = models.TimeField(verbose_name='Saída', blank=True, null=True)
    aluno = models.ForeignKey(User, models.PROTECT, related_name='usuarios')

    class Meta:
        verbose_name = 'Frequência do Aluno'
        verbose_name_plural = 'Frequências dos Alunos'

    def __str__(self) -> str:
        return '{} - {}'.format(self.dia, self.aluno)
