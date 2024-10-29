from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8002'

@given('que eu tenho os detalhes da Venda')
def step_impl(context):
    context.venda_data = {
        'cpf': '12345678910',
        'placa': 'HIJ-3C45',
        'NomeCliente': 'Jose Da Silva',
        'Veiculo': 'Uno',
        'dataVenda': '10-11-2024',
        'status': 'Aguardando Pagamento',
    }

@given('que eu tenho os detalhes atualizados da Venda')
def step_impl(context):
    context.updated_venda_data = {
        'cpf': '12345678910',
        'placa': 'HIJ-3C45',
        'NomeCliente': 'Jose Da Silva',
        'Veiculo': 'Uno',
        'dataVenda': '10-11-2024',
        'status': 'Cancelada',
    }

@when('eu faço o cadastro de uma Venda')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/vendas/create", json=context.venda_data)

@when('eu faço uma atualização de uma Venda')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/vendas/update/1", json=context.updated_venda_data)

@when('eu faço a consulta das Venda cadastras')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/vendas")

@when('eu faço a consulta de uma Venda pela placa')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/vendas/readplaca/HIJ-3C45")

@when('eu faço a consulta de uma Venda pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/vendas/readCPF/12345678910")

@when('eu faço a exclusão de uma Venda')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/vendas/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
