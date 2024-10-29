Feature: Gerenciamento de vendas

  Scenario: Adicionar um novo Venda
    Given que eu tenho os detalhes da Venda
    When eu faço o cadastro de uma Venda
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar uma Venda
    When eu faço a consulta das vendas cadastras
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar uma Venda existente
    Given que eu tenho os detalhes atualizados da Venda
    When eu faço uma atualização de uma Venda
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar uma Venda pela placa
    When eu faço a consulta de uma Venda pela placa
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar uma Venda pelo CPF
    When eu faço a consulta de uma Venda pelo CPF
    Then eu devo receber uma resposta com o código de status 200