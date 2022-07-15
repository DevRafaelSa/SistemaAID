"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################

- As Views aqui existentes tem a função de receber e entregar dados para o usuário de acordo com o método utilizado (GET, POST, PUT, DELETE).
- A View é um arquivo Python que contém a lógica de negócio do sistema.
- A lógica aplicada nas Views é responsável por manipular os dados do banco de dados e entregar para o usuário, podendo realizar atulização das informações já existentes no banco de dados, ou criar novos registros.
- Em especial, a PessoaViewSet também é responsável por criar um usuário para cada nova Pessoa cadastrada.
- A FilaViewSet realiza a busca no banco de dados do objeto Donatario, através do método GET, que ainda não tenha recebido uma doação, baseado na coluna 'recebeu_doacao' com valor 'False'.
- A FilaViewSet também poderá realizar a atualização do objeto Donatario, através do método PUT ou PATCH, para que o mesmo seja marcado como recebido uma doação.
- O Donatario/Solicitante que receber a doação, será atualizado com o valor 'True' na tabela 'recebeu_doacao'.
- Para alterar o status de um objeto, é necessário passar o ID do objeto como parâmetro na URL.
- Para mudar o status de um Donatario que recebeu uma doação para que ele retorne a ser listado na fila, é necessário passar o ID do objeto como parâmetro na URL através do método PUT ou PATCH e o valor 'False' para a coluna 'recebeu_doacao'.

ViewSets existentes:
    - EquipeViewSet 
    - PessoaViewSet
    - ParceiroViewSet
    - FerramentaViewSet
    - MobiliarioViewSet
    - EquipamentoViewSet
    - ComponenteViewSet
    - DonatarioViewSet
    - FilaDoacaoViewSet

"""

# Importando bilbiotecas, módulos e funções necessárias
from rest_framework import permissions, viewsets
from api.serializers import FilaReceberDoacaoSerializer, FilaDoacaoRecebidaSerializer, PessoaSerializer, ParceiroSerializer, EquipeSerializer, FerramentasSerializer, EquipamentosSerializer, ComponentesSerializer, MobiliarioSerializer, DonatarioSerializer
from cadastros.models import Equipe, Pessoa, Parceiro, Ferramenta, Equipamento, Mobiliario, Componente, Donatario
from users.models import User
from rest_framework.response import Response
from rest_framework import status


# Declarando a classe de viewsets para a API
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permissions_classes = [permissions.IsAuthenticated]

    # função para criar uma nova pessoa através da requisição POST via API
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # função para criar um novo usuário através da criação de nova Pessoa
    def perform_create(self, serializer):
        data = dict(self.request.data.lists())
        rgm = data['rgm'][0]
        email = data['email'][0]
        
        user = User.objects.create_user(username=rgm, email=email, password=rgm)
        user.save()
        
        serializer.save()

class FilaDocacaoRecebidaViewSet(viewsets.ModelViewSet):
    queryset = Donatario.objects.filter(recebeu_doacao=True)
    serializer_class = FilaDoacaoRecebidaSerializer
    permissions_classes = [permissions.IsAuthenticated]


class FilaReceberDoacaoViewSet(viewsets.ModelViewSet):
    queryset = Donatario.objects.filter(recebeu_doacao=False)
    serializer_class = FilaReceberDoacaoSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ParceiroViewSet(viewsets.ModelViewSet):
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer
    permissions_classes = [permissions.IsAuthenticated]


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permissions_classes = [permissions.IsAuthenticated]


class FerramentaViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentasSerializer
    permissions_classes = [permissions.IsAuthenticated]


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentosSerializer
    permissions_classes = [permissions.IsAuthenticated]


class MobiliarioViewSet(viewsets.ModelViewSet):
    queryset = Mobiliario.objects.all()
    serializer_class = MobiliarioSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponentesSerializer
    permissions_classes = [permissions.IsAuthenticated]


class DonatarioViewSet(viewsets.ModelViewSet):
    queryset = Donatario.objects.all()
    serializer_class = DonatarioSerializer
    permissions_classes = [permissions.IsAuthenticated]
