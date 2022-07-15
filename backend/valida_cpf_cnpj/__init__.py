"""
#####################################
### Author: Jorge Reis            ###
### Date: 2022-06-20              ###
### Version: 1.0                  ###
### Github: github.com/jorgereiis ###
#####################################

#### Módulo para validação de CPF e CNPJ (Cadastro Nacional de Pessoas Físicas e Jurídicas) ####

Para validação de CPF e CNPJ, utilize o módulo 'valida_cpf_cnpj'
Crie os atributos das classes utilizando o módulo 'models' do Django normalmente.

cpf = CPFField(blank=True, unique=True, error_messages={'unique': 'O CPF informado já existe.'})
cnpj = CNPJField(blank=True, unique=True, error_messages={'unique': 'O CNPJ informado já existe.'})
"""