"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################

"""
# Importando as classes de modelos
from django.contrib import admin
from .models import DoacaoDonatario, DoacaoParceiro, Equipe, Pessoa, Parceiro, Ferramenta, Mobiliario, Equipamento, Componente, Donatario

# Configurando a exibição de filtros e buscas na página de administração
class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "rgm",
        "cpf",
        "nivelexp",
        "estagiario",
        "monitor",
    ]
    list_filter = ["equipe", "estagiario", "monitor"]
    search_fields = ["rgm", "nome", "cpf"]

class ParceiroAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "pjuridica",
        "cpf",
        "cnpj",
    ]
    list_filter = ["pjuridica"]
    search_fields = ["nome", "cpf", "cnpj"]

class GruposAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "modelo",
    ]

class DonatarioAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "email",
        "cpf",
        "trabalhador",
        "estuda_unipe",
        "is_funcionario_unipe",
        "recebeu_doacao",
    ]
    list_filter = ["estuda_unipe", "is_funcionario_unipe", "sexo", "renda"]
    search_fields = ["nome", "email", "cpf", "rg", "tel", "curso_unipe"]


class DoacaoParceiroAdmin(admin.ModelAdmin):
    list_display = [
        "parceiro",
        "data_doacao",
    ]
    search_fields = ["parceiro"]


class DoacaoDonatarioAdmin(admin.ModelAdmin):
    list_display = [
        "donatario",
        "data_doacao",
    ]
    search_fields = ["donatario"]

# Registrando as classes de modelos para exibição na página de administração
admin.site.register(DoacaoDonatario, DoacaoDonatarioAdmin)
admin.site.register(DoacaoParceiro, DoacaoParceiroAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Parceiro, ParceiroAdmin)
admin.site.register(Ferramenta, GruposAdmin)
admin.site.register(Equipamento, GruposAdmin)
admin.site.register(Mobiliario, GruposAdmin)
admin.site.register(Componente, GruposAdmin)
admin.site.register(Equipe)
admin.site.register(Donatario, DonatarioAdmin)
