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
financheck-mysql
|
├── sql/
│ ├── ddl.sql
│ └── clusters.sql
│
├── dados/
│ ├── financheck_analise.csv
│ ├── financheck_padronizado.csv
│ ├── financheck_com_clusters.csv
│ ├── escolha_k.png
│ └── visualizacao_clusters.png
│
├── mineracao/
│ ├── padronizacao.py
│ ├── escolha_k.py
│ ├── kmeans_final.py
│ └── visualizacao_clusters.py
│
├── docs/
│ └── analise_clusters.md
│
└── README.md

## Como utilizar

Abra o MySQL Workbench e conecte-se ao servidor MySQL.

Em seguida, abra o arquivo `sql/ddl.sql` e execute todo o script. Ao final da execucao, sera criado o banco de dados `financheck`, com suas tabelas, relacionamentos e indices.

Para a etapa de mineracao de dados, dentro da pasta `mineracao/`, execute os scripts Python na ordem: `padronizacao.py`, `escolha_k.py`, `kmeans_final.py`, `visualizacao_clusters.py`. Requer as bibliotecas pandas, scikit-learn e matplotlib (`pip install pandas scikit-learn matplotlib`).

## Autor

Projeto desenvolvido por **Taiani** como atividade academica da disciplina de Banco de Dados.