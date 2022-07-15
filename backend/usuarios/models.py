"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################

Aqui temos a modelagem dos Usuários do sistema. O usuário é um usuário do sistema que pode acessar a API e demais recursos da aplicação.
A classe User está extendida da classe AbstractUser do Django, que é a classe que contém os dados da classe padrão do Django.

A classe UserProfile foi criada para armazenar os dados de Perfil do Usuário, caso esses dados sejam necessários.

"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from cadastros.models import validar_rgm, Pessoa

# Classe para cadastro de Usuários
class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        ("Usuário"),
        max_length=50,
        unique=True,
        help_text=(
            "Nome de usuário requer 50 caracteres ou menos. Apenas letras, dígitos e @/./+/-/_."
        ),
        validators=[username_validator],
        error_messages={
            "unique": "Já existe um usuário com esses dados.",
        },
    )
    first_name = models.CharField('Primeiro nome', max_length=150, blank=True)
    last_name = models.CharField('Último nome', max_length=150, blank=True)
    # inserir campos adicionais para o cadastro de usuários aqui
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['first_name']

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.username)
