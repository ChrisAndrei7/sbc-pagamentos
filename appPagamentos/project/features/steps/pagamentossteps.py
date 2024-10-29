from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8005'

@given('que eu tenho os detalhes do Pagamento')
def step_impl(context):
    context.pagamento_data = {
        'cpf': '12345678910',
        'placa': 'HIJ-3C45',
        'statusPagamento': 'Aguardando Pagamento',
    }

@given('que eu tenho os detalhes atualizados do Pagamento')
def step_impl(context):
    context.updated_pagamento_data = {
        'cpf': '12345678910',
        'placa': 'HIJ-3C45',
        'statusPagamento': 'Pagamento Aprovado!',
    }

@when('eu faço o cadastro de um Pagamento')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/pagamentos/create", json=context.pagamento_data)

@when('eu faço uma atualização de um Pagamento')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/pagamentos/update/1", json=context.updated_pagamento_data)

@when('eu faço a consulta dos pagamentos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pagamentos")

@when('eu faço a consulta de um Pagamento pela placa')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pagamentos/readplaca/HIJ-3C45")

@when('eu faço a consulta de um Pagamento pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pagamentos/readCPF/12345678910")

@when('eu faço a exclusão de um Pagamento')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/pagamentos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
