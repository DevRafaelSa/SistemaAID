"""
Aqui estão definidas todas as modelagens que serão realizadas no banco de dados do sistema.
Estas modelagens são definidas como classes, sendo que cada classe é um tipo de entidade, nomeadas como "Componente", "Donatario", "Equipes", "Equipamento", "Ferramenta", "Mobiliario", "Pessoa", "Parceiro".

Cada classe tem a funcionalidade de armazenar dados de um determinado tipo de entidade, sendo que cada classe tem um atributo chamado "nome" que é um nome de entidade/objeto.
Determinadas classes possuem validação para os dados de CPF e CNPJ, baseado em regras Brasileira para esses tipos de documentos.
Outras classes também possuem validação para que recebam apenas números, como os campos de RGM, CEP, RG e TELEFONE.

### MODELOS EXISTENTES ###
* Pessoa: Membros do AID, como extensionistas, professores, instrutores, alunos, etc.
* Parceiro: Pessoas que contribuem com o AID realizando doações, como empresas, instituições, ONGs, etc.
* Equipe: Grupos de pessoas que trabalham em conjunto para ajudar o AID.
* Ferramenta: Ferramentas que são utilizadas no AID e que vêm através de doações.
* Equipamento: Equipamentos que são utilizados no AID e que vêm através de doações.
* Mobiliario: Mobiliário que são utilizados no AID e que vêm através de doações.
* Componente: Componentes que são utilizados no AID e que vêm através de doações.
* Donatario: Pessoas que desejam receber doações do AID, sejam eles alunos ou membros da comunidade.

#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################
"""

# Importando bibliotecas, módulos e funcões necessárias
from tabnanny import verbose
from django.db import models
from valida_cpf_cnpj.fields import CPFField, CNPJField
from django.core.exceptions import ValidationError


# Métodos para validar apenas números nos campos RGM, CEP, RG e TELEFONE existente nas classes abaixo
def validar_rgm(value):
    if not value.isdigit():
        raise ValidationError('O RGM deve conter apenas números!')

def validar_cep(value):
    if not value.isdigit():
        raise ValidationError('O CEP deve conter apenas números!')

def validar_rg(value):
    if not value.isdigit():
        raise ValidationError('O RG deve conter apenas números!')

def validar_tel(value):
    if not value.isdigit():
        raise ValidationError('O Telefone deve conter apenas números!')


# Classe para cadastro das Equipes
class Equipe(models.Model):
    nome = models.CharField(max_length=20, unique=True, error_messages={'unique': 'Já existe uma Equipe com este nome.'})

    def __str__(self) -> str:
        return self.nome


# Classe para cadastro das Pessoas
class Pessoa(models.Model):
    nivelexp_choice = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, unique=True, error_messages={'unique': 'O e-mail informado já existe.'})
    cpf = CPFField(blank=False, unique=True, null=False, error_messages={'unique': 'O CPF informado já existe.'}, verbose_name='CPF')
    rgm = models.CharField(max_length=50, primary_key=True, blank=False, default=None, validators=[validar_rgm], unique=True, error_messages={'unique': 'O RGM informado já existe.'})
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, verbose_name='Equipe de Trabalho', blank=True, null=True, related_name='pessoas')
    nivelexp = models.CharField(max_length=1, choices=nivelexp_choice, blank=True)
    txtexp = models.TextField('Seu conhecimento sobre a área escolhida', max_length=500, blank=True)
    estagiario = models.BooleanField('Estagiário', default=False)
    monitor = models.BooleanField('Monitor', default=False)
    # Checkbox para seleção dos dias da semana de escala de trabalho
    seg = models.BooleanField("Segunda-feira")
    ter = models.BooleanField("Terça-feira")
    qua = models.BooleanField("Quarta-feira")
    qui = models.BooleanField("Quinta-feira")
    sex = models.BooleanField("Sexta-feira")
    sab = models.BooleanField("Sábado")
    ativo = models.BooleanField("Ativo", default=True)

    def __str__(self) -> str:
        return self.nome


# Classe para cadastro de Parceiros
class Parceiro(models.Model):
    pjuridica = models.BooleanField('Pessoa Jurídica', default=False)
    nome = models.CharField('Nome/Razão Social', max_length=50)
    cpf = CPFField(blank=True, null=True, error_messages={'unique': 'O CPF informado já existe.'}, verbose_name='CPF')
    cnpj = CNPJField(blank=True, null=True, error_messages={'unique': 'O CNPJ informado já existe.'}, verbose_name='CNPJ')
    resp = models.CharField('Responsável', max_length=50, blank=True)
    cep = models.CharField('CEP', max_length=9, validators=[validar_cep], blank=True)
    end = models.CharField('Endereço', max_length=50)
    num = models.CharField('Nº', max_length=50)
    comp = models.CharField('Complemento', max_length=50, blank=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    uf = models.CharField('UF', max_length=2)
    tel = models.CharField('Telefone', max_length=11, validators=[validar_tel])

    def __str__(self) -> str:
        return self.nome


# Classes para cadastro de Ferramentas, Equipamentos, Mobiliário e Componentes
class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField("Detalhes da ferramenta:", max_length=500)

    def __str__(self) -> str:
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField("Detalhes do equipamento:", max_length=500)

    def __str__(self) -> str:
        return self.nome

class Mobiliario(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField(("Detalhes da mobiliaria:"), max_length=500)

    class Meta:
        verbose_name = "Mobiliário"

    def __str__(self) -> str:
        return self.nome

class Componente(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField(("Detalhes dos componentes:"), max_length=500)

    def __str__(self) -> str:
        return self.nome


# Classe para cadastro de Donatário
class Donatario(models.Model):
    # Opções para o campo sexo
    sexo_choice = [
        ('N/A', 'Prefiro não opinar'),
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]

    # Opções para o campo estado civil
    estadocivil_choice = [
        ('solteiro','Solteiro(a)'), 
        ('casado','Casado(a)'),
        ('divorciado','Divorciado(a)'),
        ('separado','Separado(a)'),
        ('viuvo','Viúvo(a)'),
    ]

    # Opções para o campo "É estudante?"
    is_studant = [
        ('sim','Sim'),
        ('nao','Não'),
    ]

    # Opções para quantidade de pessoas na família
    qtd_familia = [
        ('1','Uma'),
        ('2','Duas'),
        ('3','Três'),
        ('4','Quatro'),
        ('5','Cinco'),
        ('6','Seis'),
        ('7','Sete'),
        ('8','Oito'),
        ('9','Nove'),
        ('10','Dez'),
    ]

    # Opções para quantidade de filhos
    qtd_filhos = [
        ('0','Nenhum'),
        ('1','Um'),
        ('2','Dois'),
        ('3','Três'),
        ('4','Quatro ou mais'),
    ]

    # Opções para Renda Familiar
    renda_familia = [
        ('renda1','Menos de R$ 1045'),
        ('renda2','De R$ 1045 até R$ 2090'),
        ('renda3','Acima de R$ 2090'),
    ]

    # Opções de notas para o campo de indicação
    nota_indica = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ]

    nome = models.CharField(max_length=50, blank=False)
    data_nasc = models.DateField('Data de nascimento', blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, error_messages={'unique': 'O e-mail informado já existe.'})
    cpf = CPFField(verbose_name = 'CPF', unique=True, blank=False, error_messages={'unique': 'O CPF informado já existe.'})
    rg = models.CharField('RG', max_length=20, validators=[validar_rg], unique=True, blank=False, error_messages={'unique': 'O RG informado já existe.'})
    emissor = models.CharField('Órgão emissor', max_length=10, blank=False)
    uf = models.CharField('UF', max_length=2, blank=False)
    nacion = models.CharField('Nacionalidade', max_length=20, blank=False)
    sexo = models.CharField('Sexo', max_length=3, choices=sexo_choice, default=sexo_choice[0], blank=False)
    estado_civil = models.CharField('Estado Civil', max_length=10, choices=estadocivil_choice, default=estadocivil_choice[0], blank=False)
    end = models.CharField('Endereço', max_length=50, blank=False)
    numero = models.CharField('Nº', max_length=6, blank=False)
    complemento = models.CharField('Complemento', max_length=50, blank=True)
    cidade = models.CharField('Cidade', max_length=25, blank=False)
    bairro = models.CharField('Bairro', max_length=25, blank=False)
    cep = models.CharField('CEP', max_length=8, validators=[validar_cep], blank=False)
    tel = models.CharField('Telefone', max_length=11, validators=[validar_tel], blank=False)
    estudante = models.CharField('Estudante?', max_length=3, choices=is_studant, default='sim')
    estuda_unipe = models.BooleanField('Estudante Unipê?')
    curso_unipe = models.CharField('Curso', max_length=50, blank=True)
    trabalhador = models.BooleanField('Trabalha?')
    local_trabalho = models.CharField('Local trabalho', max_length=50, blank=True)
    is_funcionario_unipe = models.BooleanField('Funcionário Unipê?')
    qtd_pessoas_familia = models.CharField('Tamanho da família', max_length=7, choices=qtd_familia, default=qtd_familia[0])
    qtd_filhos = models.CharField('Quantos filhos?', max_length=1, choices=qtd_filhos, default=qtd_filhos[0])
    renda = models.CharField('Renda familiar', max_length=7, choices=renda_familia, default=renda_familia[0])
    indica_unipe = models.CharField('O quanto você indicaria o AID para um conhecido?', max_length=1, choices=nota_indica, default=nota_indica[5])
    recebeu_doacao = models.BooleanField('Recebeu doação?', default=False)

    class Meta:
        verbose_name = 'Donatário'
        verbose_name_plural = 'Donatários'

    def __str__(self) -> str:
        return self.nome

class DoacaoParceiro(models.Model):
    """Cadastro de Doações"""
    parceiro = models.ForeignKey(Parceiro, models.CASCADE, related_name='doacoes')
    descricao = models.TextField(max_length=512, blank=False)
    data_doacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Doação de Parceiro"
        verbose_name_plural = "Doações de Parceiros"

    def __str__(self):
        return self.parceiro.nome


class DoacaoDonatario(models.Model):
    """Cadastro de Doações"""
    donatario = models.ForeignKey(Donatario, models.CASCADE, related_name='doacoes', limit_choices_to={'recebeu_doacao': False})
    descricao = models.TextField(max_length=512, blank=False)
    data_doacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Doação para Donatário"
        verbose_name_plural = "Doações para Donatários"

    def __str__(self):
        return self.donatario.nome
