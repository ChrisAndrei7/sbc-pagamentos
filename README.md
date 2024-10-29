<h1 align="center"> SubCars - Sistema para revenda de carros </h1>
Bem-vindo ao Sistema para revenda de carros da SubCars! Este projeto está em desenvolvimento como atividade para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de cadastro dos pagamentos</b>

# :computer: Endpoint base da aplicação
http://localhost:8005/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appPagamentos`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbPagamentos`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "pagamentos" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint deste microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appVendas/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o cadastro de um pagamento: http://localhost:8005/pagamentos/create

2 - Consultar pagamentos cadastrados: http://localhost:8005/pagamentos/

3 - Atualizar cadastro de um pagamento: http://localhost:8005/pagamentos/update/{id_do_pagamento}

4 - Deletar o cadastro de um pagamento: http://localhost:8005/pagamentos/delete/{id_da_pagamento}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento, <b>localizado na pasta appPagamentos/Documentos com nome "sbc-pagamentos.postman_collection".</b>

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
<br/>
OBS: BDD está dentro do arquivo "pagamentos.feature"

#### behave appPagamentos/project/features/pagamentos.feature

# Evidência dos testes:

#![sbc-vendas_test](link xx)
