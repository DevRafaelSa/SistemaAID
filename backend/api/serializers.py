"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################

O arquivo serializers.py é responsável por definir os serializers da API. Nele estão definidos os serializers para cada modelo da API.
"""

from django import http
from requests import Response
from rest_framework import serializers
from usuarios.models import User
from cadastros.models import Equipe, Pessoa, Parceiro, Ferramenta, Equipamento, Mobiliario, Componente, Donatario, DoacaoParceiro, DoacaoDonatario
from frequencias.models import FrequenciaAluno


class DoacaoDonatarioSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo DoacaoDonatario.
    """
    class Meta:
        model = DoacaoDonatario
        fields = [
            'id',
            'donatario', 
            'descricao',
            'data_doacao', 
        ]


class DoacaoParceiroSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo DoacaoParceiro.
    """
    class Meta:
        model = DoacaoParceiro
        fields = [
            'id',
            'parceiro',
            'descricao',
            'data_doacao',
        ]

class UserSerializer(serializers.ModelSerializer):
    """Serializers para o modelo User"""
    class Meta:
        model = User
        fields = [
            'username', 
            'password',
            ]


class FrequenciaAlunoSerializer(serializers.ModelSerializer):
    """Serializers para o modelo FrequenciaAluno"""
    class Meta:
        model = FrequenciaAluno
        fields = [
            "nome",
            "dia",
            "entrada",
            "saida",
            "aluno",
        ]


class VoltarParaFilaSerializer(serializers.Serializer):
    """Serializers para o modelo Donatario (Específico para retornar solicitante para fila de doação)"""
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(read_only=True)
    recebeu_doacao = serializers.BooleanField(default=False)

    def update(self, instance, validated_data, *args, **kwargs):
        instance.recebeu_doacao = False
        instance.save()
        return instance


class RemoverDaFilaSerializer(serializers.Serializer):
    """Serializers para o modelo Donatario (Específico para retornar solicitante para fila de doação)"""
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(read_only=True)
    recebeu_doacao = serializers.BooleanField(default=True)

    def update(self, instance, validated_data, *args, **kwargs):
        instance.recebeu_doacao = True
        instance.save()
        return instance


class PessoaSerializer(serializers.ModelSerializer):
    """Serializers para o modelo Pessoa"""
    class Meta:
        model = Pessoa
        fields = [
            "nome",
            "email",
            "cpf",
            "rgm",
            "equipe",
            "nivelexp",
            "txtexp",
            "estagiario",
            "monitor",
            "seg",
            "ter",
            "qua",
            "qui",
            "sex",
            "sab",
        ]



class ParceiroSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Parceiro"""
    class Meta:
        model = Parceiro
        fields = [
            "id",
            "pjuridica",
            "nome",
            "cpf",
            "cnpj",
            "resp",
            "cep",
            "end",
            "num",
            "comp",
            "bairro",
            "cidade",
            "uf",
            "tel",
        ]


class EquipeSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Equipe"""
    class Meta:
        model = Equipe
        fields = [
            "id",
            "nome",
        ]


class FerramentasSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Ferramenta"""
    class Meta:
        model = Ferramenta
        fields = [
            "id",
            "nome",
            "modelo",
            "descricao",
        ]


class EquipamentosSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Equipamento"""
    class Meta:
        model = Equipamento
        fields = [
            "id",
            "nome",
            "modelo",
            "descricao",
        ]


class MobiliarioSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Mobiliario"""
    class Meta:
        model = Mobiliario
        fields = [
            "id",
            "nome",
            "modelo",
            "descricao",
        ]


class ComponentesSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Componente"""
    class Meta:
        model = Componente
        fields = [
            "id",
            "nome",
            "modelo",
            "descricao",
        ]


class DonatarioSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Donatario (Específico para criar um novo solicitante de doação)"""
    class Meta:
        model = Donatario
        fields = [
            "id",
            "nome",
            "data_nasc",
            "email",
            "cpf",
            "rg",
            "emissor",
            "uf",
            "nacion",
            "sexo",
            "estado_civil",
            "end",
            "numero",
            "complemento",
            "cidade",
            "bairro",
            "cep",
            "tel",
            "estudante",
            "estuda_unipe",
            "curso_unipe",
            "trabalhador",
            "local_trabalho",
            "is_funcionario_unipe",
            "qtd_pessoas_familia",
            "qtd_filhos",
            "renda",
            "indica_unipe",
        ]
