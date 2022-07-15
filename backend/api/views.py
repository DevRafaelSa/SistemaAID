"""
* As Views aqui existentes tem a função de receber e entregar dados para o usuário de acordo com o método utilizado (GET, POST, PUT, DELETE).
* A View é um arquivo Python que contém a lógica de negócio do sistema.
* A lógica aplicada nas Views é responsável por manipular os dados do banco de dados e entregar para o usuário, podendo realizar atulização das informações já existentes no banco de dados, ou criar novos registros.

ViewSets existentes:
    * ComponenteViewSet - Cria, atualiza, lista e exclui componentes.
    * ConsultaFrequenciaViewSet - Lista as frequências existentes.
    * DonatarioViewSet - Cria, atualiza, lista e exclui donatários.
    * EquipamentoViewSet - Cria, atualiza, lista e exclui equipamentos.
    * EquipeViewSet - Cria, atualiza, lista e exclui equipes.
    * FerramentaViewSet - Cria, atualiza, lista e exclui ferramentas.
    * MobiliarioViewSet - Cria, atualiza, lista e exclui mobiliários.
    * PessoaViewSet - Cria, atualiza, lista e exclui pessoas.
    * ParceiroViewSet - Cria, atualiza, lista e exclui parceiros.
    * RegistraFrequenciaViewSet - Registra uma frequência.
    * VoltarParaFilaViewSet - Volta um solicitante para a fila.

#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-26              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################
"""
# Importando do Django, Python e outros módulos necessários:
from genericpath import exists
from itertools import count
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
import datetime

# Importando dos módulos do projeto:
from frequencias.models import FrequenciaAluno
from usuarios.models import User
from cadastros import models
from api import serializers


class ComponenteViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR COMPONENTES
    Classe para criar e listar Componentes do sistema."""
    queryset = models.Componente.objects.all().order_by('nome')
    serializer_class = serializers.ComponentesSerializer
    permissions_classes = [permissions.IsAuthenticated]


class FrequenciaCreateViewSet(viewsets.ModelViewSet):
    """
    # REALIZAR REGISTRO DA FREQUÊNCIA DO ALUNO.
    Classe contendo a função `create()` estendida do Django Rest Framework para realizar o registro da frequência do aluno.

    * Permitido apenas o método POST;
    * Requer obrigatoriamente os parâmetros `username` e `password` na requisição (username e senha do aluno serão definidos pelo sistema durante a criação do registro da Pessoa, que terão seus valores iguais ao RGM);
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permissions_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = dict(self.request.data.lists())
        username = data['username'][0]
        password = data['password'][0]

        try:
        # Laço para verificar se a senha do aluno é válida.
            if check_password(password, User.objects.get(username=username).password):
                frequencia = FrequenciaAluno.objects.filter(dia=datetime.date.today(), aluno__username=username)
                # Se a senha for válida, verifica se o aluno já possui uma frequência registrada para o dia atual.
                # Caso sim, registra a frequência de saída.
                if frequencia.count() > 0 and frequencia.count() < 2:
                    fname = User.objects.get(username=username).first_name
                    lname = User.objects.get(username=username).last_name
                    if lname == '':
                        nome = fname
                    else:
                        nome = fname + ' ' + lname
                    saida = FrequenciaAluno.objects.create(saida=datetime.datetime.now().time().strftime("%H:%M:%S"), aluno=User.objects.get(username=username), nome=nome)
                    saida.save()
                    return Response({"Sucesso": "Sua saída foi registrada. Até mais, {}!".format(fname)}, status=status.HTTP_201_CREATED)
                # Caso ainda não exista ao menos uma frequência registrada, registra a frequência de entrada.
                elif frequencia.count() == 0 or frequencia.count() == 1:
                    fname = User.objects.get(username=username).first_name
                    lname = User.objects.get(username=username).last_name
                    nome = fname + ' ' + lname
                    entrada = FrequenciaAluno.objects.create(entrada=datetime.datetime.now().time().strftime("%H:%M:%S"), aluno=User.objects.get(username=username), nome=nome)
                    entrada.save()
                    return Response({"Sucesso": "Sua entrada foi registrada. Bem-vindo, {}!".format(fname)}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"Aviso":"Você já registrou sua entrada e saída hoje. Por favor, tente novamente amanhã!"})
            else:   
                # Se a senha não for válida, retorna um erro.
                return Response({'Erro': 'Usuário ou senha inválidos!'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            # Se o usuário não existir ou for inválido, retorna um erro.
            return Response({'Erro': 'Usuário ou senha inválidos!'}, status=status.HTTP_401_UNAUTHORIZED)
        


class FrequenciaConsultViewSet(viewsets.ModelViewSet):
    """
    # CONSULTA RELATÓRIO DE FREQUÊNCIA DE ALUNOS.
    Classe contendo função `list()` estendida da classe ModelViewSet, do Django Rest Framework, para listar as frequências de um aluno baseado nos parâmetros passados na URL.

    * Permitido apenas o método GET;
    * Com a requisição GET, o retorno será uma lista com as frequências de acordo com os parâmetros passados, podendo ser:
        * O aluno (rgm ou nome do usuário cadastrado no sistema);
        * A data de início - é esperado um valor para data inicial no formado YYYY-MM-DD, podendo ser separado por hífens(-) ou barras(/);
        * A data de fim - é esperado um valor para data final no formado YYYY-MM-DD, podendo ser separado por hífens(-) ou barras(/);
    * Caso não seja passado nenhum parâmetro, a função lista todas as frequências existentes no Banco de Dados;
    * Caso seja passado apenas o aluno, a função lista todas as frequências do aluno informado;
    * Caso seja passado apenas as datas de início e fim, a função lista todas as frequências entre as datas informadas tendo como limite o período de até 30 dias;
    * Caso seja passado o aluno e as datas de início e fim, a função lista todas as frequências do aluno informado entre as datas informadas.
    """
    queryset = FrequenciaAluno.objects.all()
    serializer_class = serializers.FrequenciaAlunoSerializer
    permissions_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        data = dict(self.request.query_params.lists())

        # Laço principal para retornar consulta se houver parâmetros `data_incial`, `data_final` e `aluno` na URL
        if 'data_inicial' in data and 'data_final' in data and 'aluno' in data:
            dt1 = data['data_inicial'][0]
            dt2 = data['data_final'][0]
            aluno = data['aluno'][0]
            # Verificando o formato das datas, convertendo para tipo datetime e fazendo o calculo da diferença entre os dias
            if '-' in dt1 and '-' in dt2:
                dt1 = dt1.split('-')
                dt2 = dt2.split('-')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            else:
                dt1 = dt1.split('/')
                dt2 = dt2.split('/')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            # Retornando erro caso o período entre as datas seja maior que 30 dias
            if dias > 30:
                return Response({"erro": "Permitido apenas busca para um intervalo de até 30 dias."}, status=status.HTTP_400_BAD_REQUEST)
            # Retornando erro caso a data inicial seja maior que a data final
            elif dias < 0:
                return Response({"erro": "Data inicial é maior do que a Data final"}, status=status.HTTP_400_BAD_REQUEST)
            # Se estiver tudo ok, retorna a consulta
            else:
                if aluno.isnumeric():
                    queryset = FrequenciaAluno.objects.filter(aluno=aluno, dia__gte = dt1, dia__lte = dt2)
                else:
                    queryset = FrequenciaAluno.objects.filter(nome__icontains=aluno, dia__gte = dt1, dia__lte = dt2)

                serializer = serializers.FrequenciaAlunoSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        # Laço secundário para retornar consulta se houver apenas os parâmetros `data_incial` e `data_final` na URL
        elif 'data_inicial' in data and 'data_final' in data:
            dt1 = data['data_inicial'][0]
            dt2 = data['data_final'][0]
            # Verificando o formato das datas, convertendo para tipo datetime e fazendo o calculo da diferença entre os dias
            if '-' in dt1 and '-' in dt2:
                dt1 = dt1.split('-')
                dt2 = dt2.split('-')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            else:
                dt1 = dt1.split('/')
                dt2 = dt2.split('/')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            # Retornando erro caso o período entre as datas seja maior que 30 dias
            if dias > 30:
                return Response({"erro": "Permitido apenas busca para um intervalo de até 30 dias."}, status=status.HTTP_400_BAD_REQUEST)
            # Retornando erro caso a data inicial seja maior que a data final
            elif dias < 0:
                return Response({"erro": "Data inicial é maior do que a Data final"})
            # Se estiver tudo ok, retorna a consulta
            else:
                queryset = FrequenciaAluno.objects.filter(dia__gte = dt1, dia__lte = dt2)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        # Laço final para retornar consulta se houver apenas o parâmetro `aluno` na URL
        elif 'aluno' in data:
            aluno = data['aluno'][0]
            queryset = FrequenciaAluno.objects.filter(aluno=aluno).order_by('dia')
            serializer = serializers.FrequenciaAlunoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Caso não seja passado nenhum parâmetro, retorna todos os registros
        else:
            queryset = FrequenciaAluno.objects.all().order_by('dia')
            serializer = serializers.FrequenciaAlunoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DoacaoParceiroViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR DOAÇÕES
    Classe contendo as funções `list()` e `create()` para a API de listagem e criação de doações.

    * Para criação de uma nova doação, é necessário passar os seguintes parâmetros na requisição:
        * `id`: ID do parceiro já existente no sistema
        * `descricao`: Descrição da doação
    
    * Para consultar os registros das doações, é necessário passar os seguintes parâmetros na requisição:
        * `parceiro` : Podendo ser passado o CPF, CNPJ ou Nome do parceiro (não utilizar máscara para cpf e cnpj).
        * `data_inicial` : Data inicial da doação, no formato `YYYY-MM-DD`.
        * `data_final` : Data final da doação, no formato `YYYY-MM-DD`.
        * O intervalo entre as datas deve ser menor ou igual a 30 dias.
        * Caso não seja passado nenhum parâmetro, retorna todos os registros.
    """
    queryset = models.DoacaoParceiro.objects.all()
    serializer_class = serializers.DoacaoParceiroSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Função estendida do ModelViewSet para criação de novas doações."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """Função estendida do ModelViewSet para listagem de doações."""
        data = dict(self.request.query_params.lists())
        # Retornando consulta filtrando por aluno e período
        if 'data_inicial' in data and 'data_final' in data and 'parceiro' in data:
            dt1 = data['data_inicial'][0]
            dt2 = data['data_final'][0]
            parceiro = data['parceiro'][0]
            # Convertendo as datas passadas na URL para o formato datetime no padrão YYYY-MM-DD
            if '-' in dt1 and '-' in dt2:
                dt1 = dt1.split('-')
                dt2 = dt2.split('-')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            else:
                dt1 = dt1.split('/')
                dt2 = dt2.split('/')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            # Retornando erro caso o período entre as datas seja maior que 30 dias
            if dias > 30:
                return Response({"erro": "Permitido apenas busca para um intervalo de até 30 dias."}, status=status.HTTP_400_BAD_REQUEST)
            # Retornando erro caso a data inicial seja maior que a data final
            elif dias < 0:
                return Response({"erro": "Data inicial é maior do que a Data final"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if parceiro.isnumeric() and len(parceiro) == 11:
                    queryset = models.DoacaoParceiro.objects.filter(parceiro__cpf__icontains=parceiro, data_doacao__gte = dt1, data_doacao__lte = dt2).order_by('data_doacao')
                elif parceiro.isnumeric() and len(parceiro) == 14:
                    queryset = models.DoacaoParceiro.objects.filter(parceiro__cnpj__icontains=parceiro, data_doacao__gte = dt1, data_doacao__lte = dt2).order_by('data_doacao')
                else:
                    queryset = models.DoacaoParceiro.objects.filter(parceiro__nome__icontains=parceiro, data_doacao__gte = dt1, data_doacao__lte = dt2).order_by('data_doacao')
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif 'data_inicial' in data and 'data_final' in data:
            dt1 = data['data_inicial'][0]
            dt2 = data['data_final'][0]
            # Convertendo as datas passadas na URL para o formato datetime no padrão YYYY-MM-DD
            if '-' in dt1 and '-' in dt2:
                dt1 = dt1.split('-')
                dt2 = dt2.split('-')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            else:
                dt1 = dt1.split('/')
                dt2 = dt2.split('/')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            # Retornando erro caso o período entre as datas seja maior que 30 dias
            if dias > 30:
                return Response({"erro": "Permitido apenas busca para um intervalo de até 30 dias."}, status=status.HTTP_400_BAD_REQUEST)
            # Retornando erro caso a data inicial seja maior que a data final
            elif dias < 0:
                return Response({"erro": "Data inicial é maior do que a Data final"})
            # Retornando consulta apenas por data
            else:
                queryset = models.DoacaoParceiro.objects.filter(data_doacao__gte = dt1, data_doacao__lte = dt2).order_by('data_doacao')
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif 'parceiro' in data:
            parceiro = data['parceiro'][0]
            if parceiro.isnumeric() and len(parceiro) == 11:
                queryset = models.DoacaoParceiro.objects.filter(parceiro__cpf__icontains=parceiro).order_by('data_doacao')
            elif parceiro.isnumeric() and len(parceiro) == 14:
                queryset = models.DoacaoParceiro.objects.filter(parceiro__cnpj__icontains=parceiro).order_by('data_doacao')
            else:
                queryset = models.DoacaoParceiro.objects.filter(parceiro__nome__icontains=parceiro).order_by('data_doacao')
            serializer = serializers.DoacaoParceiroSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Retornando consulta com todos os dados existentes
        else:
            queryset = models.DoacaoParceiro.objects.all().order_by('data_doacao')
            serializer = serializers.DoacaoParceiroSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class DoacaoDonatarioViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR DOAÇÕES PARA DONATARIOS
    Classe contendo as funções `create()` e `list()` estendidas do ModelViewSet para criar e listar doações para donatários.

    * Para criar uma nova doação é necessário informar o ID do donatário no campo `donatario` e os itens da doação no campo `descricao`;
    * Após a criação, o donatário tem a flag `recebeu_doacao` marcada como `True`;
    * Só estarão disponíveis para receber uma doação os donatários que tenham a flag `recebeu_doacao` marcada como `False`;
    * Para listar as doações basta enviar uma requisição com o método `GET` e obter como resposta um JSON com todas as doações;
    * Para listar as doações por período basta passar as datas no formato `YYYY-MM-DD` no campo `data_inicial` e `data_final`;"""
    queryset = models.DoacaoDonatario.objects.all()
    serializer_class = serializers.DoacaoDonatarioSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Função estendida do ModelViewSet para criação de novas doações."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        donatario = models.Donatario.objects.filter(id=serializer.data['donatario']).update(recebeu_doacao=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        """Função estendida do ModelViewSet para listagem de doações."""
        data = dict(self.request.query_params.lists())
        # Retornando consulta filtrando por aluno e período
        if 'data_inicial' in data and 'data_final' in data:
            dt1 = data['data_inicial'][0]
            dt2 = data['data_final'][0]
            parceiro = data['donatario'][0]
            # Convertendo as datas passadas na URL para o formato datetime no padrão YYYY-MM-DD
            if '-' in dt1 and '-' in dt2:
                dt1 = dt1.split('-')
                dt2 = dt2.split('-')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            else:
                dt1 = dt1.split('/')
                dt2 = dt2.split('/')
                dt1 = datetime.datetime(int(dt1[0]), int(dt1[1]), int(dt1[2]))
                dt2 = datetime.datetime(int(dt2[0]), int(dt2[1]), int(dt2[2]))
                dias = (dt2 - dt1).days
            # Retornando erro caso o período entre as datas seja maior que 30 dias
            if dias > 30:
                return Response({"erro": "Permitido apenas busca para um intervalo de até 30 dias."}, status=status.HTTP_400_BAD_REQUEST)
            # Retornando erro caso a data inicial seja maior que a data final
            elif dias < 0:
                return Response({"erro": "Data inicial é maior do que a Data final"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                queryset = models.DoacaoDonatario.objects.filter(data_doacao__gte = dt1, data_doacao__lte = dt2).order_by('data_doacao')
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = models.DoacaoDonatario.objects.all().order_by('data_doacao')
            serializer = serializers.DoacaoDonatarioSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class DonatarioViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR DONATÁRIOS
    Classe para criar e listar Donatarios do sistema."""
    queryset = models.Donatario.objects.all()
    serializer_class = serializers.DonatarioSerializer
    permissions_classes = [permissions.IsAuthenticated]


class EquipamentoViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR EQUIPAMENTOS
    Classe para criar e listar Equipamentos do sistema."""
    queryset = models.Equipamento.objects.all()
    serializer_class = serializers.EquipamentosSerializer
    permissions_classes = [permissions.IsAuthenticated]


class EquipeViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR EQUIPES
    Classe para criar e listar Equipes do sistema.
    """
    queryset = models.Equipe.objects.all()
    serializer_class = serializers.EquipeSerializer
    permissions_classes = [permissions.IsAuthenticated]


class FerramentaViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR FERRAMENTAS
    Classe para criar e listar Ferramentas do sistema."""
    queryset = models.Ferramenta.objects.all()
    serializer_class = serializers.FerramentasSerializer
    permissions_classes = [permissions.IsAuthenticated]


class MobiliarioViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR MOBILIARIOS
    Classe para criar e listar Mobiliarios do sistema."""
    queryset = models.Mobiliario.objects.all()
    serializer_class = serializers.MobiliarioSerializer
    permissions_classes = [permissions.IsAuthenticated]


class PessoaViewSet(viewsets.ModelViewSet):
    """
    # CRIAÇÃO DE PESSOAS E USUÁRIOS
    Classe contendo `create()` estendida do Django Rest Framework para criar um Usuário para cada nova Pessoa cadastrada.

    * Permitido todo os métodos de CRUD.
    * Caso não haja erros na validação do serializer, a função create é chamada para criar um usuário para cada nova Pessoa cadastrada.
    * O usuário é criado tendo como username e password o RGM da Pessoa.
    """

    queryset = models.Pessoa.objects.all()
    serializer_class = serializers.PessoaSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            rgm = request.data['rgm']
            email = request.data['email']
            nomecompleto = request.data['nome']
            valida_usuario = User.objects.filter(username=rgm)
            if ' ' in nomecompleto:
                nome_list = nomecompleto.split(' ')
                nome = nome_list[0]
                sobrenome = nome_list[len(nome_list) - 1]
            else:
                nome = nomecompleto
                sobrenome = ''

            if valida_usuario:
                content = {'erro': 'Já existe um usuário com esse RGM em nossos registros'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:
                self.perform_create(serializer)
                user = User.objects.create_user(username=rgm, email=email, password=rgm, first_name=nome, last_name=sobrenome)
                user.save()
                token = Token.objects.create(user=user)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ParceiroViewSet(viewsets.ModelViewSet):
    """
    # CRIAR E LISTAR PARCEIROS
    Classe para criar e listar Parceiros do sistema.
    Esta classe contém a função `create()` estendida do Django Rest Framework para validar e criar um novo Parceiro.

    * Permitido todos do métodos do CRUD;
    * Requer obrigatoriamente que sejam passados os seguintes parametros na requisição:
        * `pjuridica` - Se o parceiro é Pessoa Jurídica ou Pessoa Física;
        * `cpf` - Se o parceiro é Pessoa Física, este será obrigatório se o parceiro for Pessoa Física;
        * `cnpj` - Se o parceiro é Pessoa Jurídica, este será obrigatório se o parceiro for Pessoa Jurídica;
        * `nome` : nome do parceiro ou razão social do parceiro;
        * `end` : endereço do parceiro;
        * `num` : número do endereço do parceiro;
        * `bairro` : bairro do parceiro;
        * `cidade` : cidade do parceiro;
        * `uf` : uf do parceiro;
        * `tel` : telefone do parceiro;
    """

    queryset = models.Parceiro.objects.all()
    serializer_class = serializers.ParceiroSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['pjuridica']:
            pjuridica = request.data['pjuridica']
            if pjuridica == 'True' or pjuridica == 'true' or pjuridica == True:
                pjuridica = True
        else:
            pjuridica = False

        if pjuridica == False:
            if request.data['cpf'] == '':
                return Response({"Erro": "O campo CPF é obrigatório para Pessoa Física. Tente novamente!"}, status=status.HTTP_400_BAD_REQUEST, headers=headers)
            else:
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            if request.data['cnpj'] == '':
                return Response({"Erro": "O campo CNPJ é obrigatório para Pessoa Jurídica. Tente novamente!"}, status=status.HTTP_400_BAD_REQUEST, headers=headers)
            else:
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VoltarParaFilaViewSet(viewsets.ModelViewSet):
    """
    # RETORNA UM DONATÁRIO PARA A FILA DE ESPERA.
    Classe para listar e alterar o status de `recebeu_doacao` para `False`, e permitir que o donatário solicitante volte para a fila de espera das doações.

    * Permitido apenas os métodos GET e PATCH;
    * Requer obrigatoriamente que seja passado o parâmetro `id` na URL;
    """

    queryset = models.Donatario.objects.filter(recebeu_doacao=True)
    serializer_class = serializers.VoltarParaFilaSerializer
    permissions_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch']


class RemoverDaFilaViewSet(viewsets.ModelViewSet):
    """
    # REMOVE UM DONATÁRIO DA A FILA DE ESPERA.
    Classe para listar e alterar o status de `recebeu_doacao` para `True`, e permitir que o donatário solicitante não seja mais listado na fila de espera das doações.

    * Permitido apenas os métodos GET e PATCH;
    * Requer obrigatoriamente que seja passado o parâmetro `id` na URL;
    """

    queryset = models.Donatario.objects.filter(recebeu_doacao=False)
    serializer_class = serializers.RemoverDaFilaSerializer
    permissions_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch']