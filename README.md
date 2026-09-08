# FinanCheck

## Sobre o projeto

O FinanCheck é um projeto acadêmico desenvolvido para a disciplina de Banco de Dados. Seu objetivo é modelar e implementar um banco de dados relacional para auxiliar no gerenciamento financeiro pessoal, com uma etapa complementar de mineração de dados (clusterização de perfis financeiros de usuários).

## Funcionalidade

O banco de dados permite:

- Cadastro de usuário;
- Cadastro de categorias de receitas e despesas;
- Registro de receitas;
- Controle de metas financeiras.

## Mineracao de Dados

A partir dos dados extraidos da view `vw_analise_financeira`, foi realizada uma analise de clusterizacao (K-Means) para identificar perfis financeiros entre os usuarios:

- Analise exploratoria dos dados (qualidade, distribuicao, correlacoes);
- Padronizacao das variaveis com StandardScaler;
- Escolha do numero de clusters (K=4) via metodo do cotovelo e silhouette score;
- Execucao do K-Means e interpretacao dos 4 perfis identificados;
- Visualizacao dos clusters via PCA.

Documentacao completa da analise em [`docs/analise_clusters.md`](docs/analise_clusters.md).

## Tecnologias utilizadas

- MySQL 8
- SQL (DDL)
- MySQL Workbench
- Python (pandas, scikit-learn, matplotlib)

## Estrutura do projeto

## Estrutura do projeto

```
financheck-mysql
|
├── sql/
│   ├── ddl.sql
│   └── clusters.sql
│
├── dados/
│   ├── financheck_analise.csv
│   ├── financheck_padronizado.csv
│   ├── financheck_com_clusters.csv
│   ├── escolha_k.png
│   └── visualizacao_clusters.png
│
├── mineracao/
│   ├── padronizacao.py
│   ├── escolha_k.py
│   ├── kmeans_final.py
│   ├── visualizacao_clusters.py
│   └── carregar_clusters_mysql.py
│
├── docs/
│   ├── analise_clusters.md
│   └── documentacao_projeto.md
│
└── README.md
```

## Como utilizar

Abra o MySQL Workbench e conecte-se ao servidor MySQL.

Em seguida, abra o arquivo `sql/ddl.sql` e execute todo o script. Ao final da execucao, sera criado o banco de dados `financheck`, com suas tabelas, relacionamentos e indices.

Para a etapa de mineracao de dados, dentro da pasta `mineracao/`, execute os scripts Python na ordem: `padronizacao.py`, `escolha_k.py`, `kmeans_final.py`, `visualizacao_clusters.py`. Requer as bibliotecas pandas, scikit-learn e matplotlib (`pip install pandas scikit-learn matplotlib`).

Para persistir o resultado da segmentacao no banco de dados, execute `sql/clusters.sql` no Workbench (cria a tabela `cluster_usuario`) e em seguida `mineracao/carregar_clusters_mysql.py` (requer `mysql-connector-python` e `python-dotenv`, alem de um arquivo `.env` na raiz do projeto com a variavel `DB_PASSWORD`).

## Documentacao adicional

- [`docs/analise_clusters.md`](docs/analise_clusters.md): analise exploratoria, padronizacao, escolha do numero de clusters e interpretacao dos perfis identificados.
- [`docs/documentacao_projeto.md`](docs/documentacao_projeto.md): requisitos funcionais e nao funcionais, estimativa de custos, diagrama UML de casos de uso e atualizacao do dicionario de dados.
