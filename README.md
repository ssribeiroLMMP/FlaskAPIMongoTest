# Perguntas

## 1) Você acha que este código está estruturado, legível e escalável?

Acredito que a estrutura está confusa, pois os nomes das variáveis repetidos em contextos diferentes, em e linguagens diferentes, dificultam o entendimento da lógica do código e suas funções para quem nunca utilizou o nem software de banco de dados nem o framework escolhidos para esta aplicação.
Facilitaria a legibilidade do mesmo definir responsabilidades únicas para cada módulo da aplicação. O que também diz respeito da escalabilidades.
Um modo de escalar a aplicação seria criando uma Classe para instanciar novos objetos que populariam o banco de dados e validando os atributos recebidos e os tipos de valores de cada chave do objeto.

## 2) O que você mudaria nos arquivos e na estrutura de pastas para melhorá-lo nesse sentido?

Como comentado na questão acima, organizar os arquivos conforme suas responsabilidades em módulos e pacotes estruturados facilitam o entendimento e compreensão da aplicação de modo mais eficaz.
Nomear os pactos e módulos como já é de uso corrente na comunidade também podem facilitar e agilizar o desenvolvimento da aplicação quando de uso de outros desenvolvedores.
Como já pacificado pela comunidade, a estrutura da aplicação poderia compreender:

- um módulo específico para criar cada classe necessária à criação de tabelas para banco de dados, com as validações necessárias tipando os valores a serem retornados por cada atributo da classe;
- um módulo específico para se ocupar das rotas na API, via client;
- um módulo específico para a lógica em cada requisição HTML, seguindo as regras de CRUD e validando os dados recebidos, alterados, além das permissões para cada método de requisição;
- um módulo específico para as queries no banco de dados.

Para escalar mais a aplicação, cada módulo pode estar dentro de pacotes que receberão os módulos correspondentes conforme suas responsabilidades específicas, tendo como orientação os princípios da SOLID.

## 3) Quanto a arquitetura API e sua conteinerização, liste as brechas de segurança que você identificou neste código? Como você as resolveria?

A respeito da segurança, entendo que não é indicado deixar dados de um user do banco de dados exposto. O ideal é criar um arquivo com os atributos obrigatórios para acessar o banco de dados e disponibilizá-lo como "dica". No docker-compose lista-se apenas com valores genéricos fornecidos, geralmente, nas documentações disponíveis no hub do próprio Docker.
Ainda sobre segurança, ter volumes compartilhados pode não ser uma boa estratégia durante o desenvolvimento da aplicação, pois o mesmo apenas garante que as informações nas tabelas do banco de dados se manterão pela conexão local.
Particularmente, não consegui acessar o banco de dados pois não tinha certeza se era recomendado alterar o docker-compose, que está com versão antiga, que está com framework e software de db que desconheço. O que me dificultou muito definir como seriam as queries necessárias para realizar as solicitações do cliente.
