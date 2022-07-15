"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################
"""
from rest_framework.routers import DefaultRouter
from . import views

# Variável que guarda nome do app onde está a modelagem a ser utilizada na API
app_name = "cadastros"

# Declarando o router para a API
router = DefaultRouter(trailing_slash=False)

router.register(r"componente", views.ComponenteViewSet, basename="componente")
router.register(r"donatario", views.DonatarioViewSet, basename="donatario")
router.register(r"doacao-parceiro", views.DoacaoParceiroViewSet, basename="doacaoparceiro")
router.register(r"doacao-donatario", views.DoacaoDonatarioViewSet, basename="doacaodonatario")
router.register(r"equipe", views.EquipeViewSet, basename="equipe")
router.register(r"equipamento", views.EquipamentoViewSet, basename="equipamento")
router.register(r"frequencia-consulta", views.FrequenciaConsultViewSet, basename="consultafrequencia")
router.register(r"frequencia-criar", views.FrequenciaCreateViewSet, basename="registrafrequencia")
router.register(r"ferramenta", views.FerramentaViewSet, basename="ferramenta")
router.register(r"mobiliario", views.MobiliarioViewSet, basename="mobiliario")
router.register(r"pessoa", views.PessoaViewSet, basename="pessoa")
router.register(r"parceiro", views.ParceiroViewSet, basename="parceiro")
router.register(r"voltar-donatario-fila", views.VoltarParaFilaViewSet, basename="voltarparafila")
router.register(r"remover-donatario-fila", views.RemoverDaFilaViewSet, basename="removerdafila")

urlpatterns = router.urls