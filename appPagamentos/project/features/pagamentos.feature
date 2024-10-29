Feature: Gerenciamento de pagamentos

  Scenario: Adicionar um novo pagamento
    Given que eu tenho os detalhes do Pagamento
    When eu faço o cadastro de um Pagamento
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar uma Pagamento
    When eu faço a consulta dos pagamentos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Pagamento existente
    Given que eu tenho os detalhes atualizados do Pagamento
    When eu faço uma atualização de um Pagamento
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Pagamento pela placa
    When eu faço a consulta de um Pagamento pela placa
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Pagamento pelo CPF
    When eu faço a consulta de um Pagamento pelo CPF
    Then eu devo receber uma resposta com o código de status 200