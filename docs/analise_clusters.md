# Analise de Clusters - FinanCheck

Documento de acompanhamento do processo de mineracao de dados do projeto FinanCheck, cobrindo analise exploratoria, preparacao dos dados, escolha do numero de clusters e interpretacao dos grupos formados.

## 1. Analise Exploratoria

Base de dados: 50 registros, 9 colunas, extraidos da view vw_analise_financeira do banco financheck.

Verificacao de qualidade: 0 valores ausentes, 0 registros duplicados, 2 saldos negativos identificados (nao removidos, tratados como caracteristica valida do perfil financeiro).

Estatisticas descritivas das variaveis numericas:

| Variavel | Media | Mediana | Minimo | Maximo | Desvio padrao |
|---|---|---|---|---|---|
| total_receitas | 1774.47 | 1150.00 | 185.75 | 4600.00 | 1444.34 |
| total_despesas | 360.11 | 227.80 | 28.50 | 1600.00 | 369.29 |
| saldo | 1414.36 | 930.10 | -100.00 | 4360.00 | 1258.28 |
| percentual_meta | 40.84 | 33.33 | 20.00 | 100.00 | 22.82 |

Foi identificada correlacao forte entre total_receitas e saldo (aproximadamente 0.972), esperada pois o saldo deriva diretamente de receitas e despesas.

total_despesas e percentual_meta apresentam assimetria positiva elevada, o que reforcou a necessidade de padronizacao antes da mineracao.

## 2. Preparacao dos Dados para o K-Means

Variaveis utilizadas no agrupamento: total_receitas, total_despesas, saldo e percentual_meta. As colunas id_usuario e usuario foram excluidas por serem identificadores, e status_meta foi reservada para interpretacao posterior dos grupos, nao utilizada como variavel de entrada.

As quatro variaveis foram padronizadas com StandardScaler (media 0, desvio padrao 1), necessario pois estavam em escalas muito diferentes (saldo chegando a milhares, percentual_meta limitado a 100).

## 3. Escolha do Numero de Clusters (K)

Foram testados valores de K de 2 a 10, avaliando o metodo do cotovelo (inercia) e o silhouette score:

| K | Inercia | Silhouette |
|---|---|---|
| 2 | 94.88 | 0.5414 |
| 3 | 55.35 | 0.6098 |
| 4 | 31.47 | 0.6526 |
| 5 | 24.96 | 0.6063 |
| 6 | 18.47 | 0.6070 |
| 7 | 15.06 | 0.4227 |
| 8 | 12.05 | 0.4191 |
| 9 | 9.63 | 0.4295 |
| 10 | 8.08 | 0.4113 |

O cotovelo aparece visualmente em K=4, ponto onde a queda da inercia desacelera. O silhouette score confirma essa escolha, atingindo seu valor mais alto (0.6526) tambem em K=4, caindo de forma acentuada a partir de K=7. Com os dois metodos concordando, foi definido K=4 para o agrupamento final.

## 4. Interpretacao dos Clusters

O K-Means foi executado com K=4 sobre as variaveis padronizadas. Resultado:

| Cluster | Usuarios | Receita media | Despesa media | Saldo medio | Meta media | Status |
|---|---|---|---|---|---|---|
| 0 | 28 | 789.03 | 203.84 | 585.19 | 33.61% | Todos EM_ANDAMENTO |
| 1 | 3 | 4200.00 | 1550.00 | 2650.00 | 36.25% | Todos EM_ANDAMENTO |
| 2 | 13 | 3565.38 | 430.55 | 3134.83 | 30.16% | Todos EM_ANDAMENTO |
| 3 | 6 | 1280.08 | 341.82 | 938.27 | 100.00% | Todos CONCLUIDA |

Perfis identificados:

- Cluster 0 (renda baixa): maior grupo, receita e despesa baixas, metas ainda distantes de conclusao.
- Cluster 1 (alta renda, alto gasto): grupo pequeno (3 usuarios), receita e despesa elevadas, menor eficiencia de poupanca proporcional.
- Cluster 2 (alta capacidade de poupanca): receita alta, despesa baixa, maior saldo medio entre os grupos, mas progresso de meta ainda baixo.
- Cluster 3 (metas concluidas): unico grupo com 100% de progresso em todas as metas, coincide exatamente com os usuarios de status CONCLUIDA.

## 5. Observacao Importante sobre os Resultados

O algoritmo formou os clusters usando apenas total_receitas, total_despesas, saldo e percentual_meta, sem acesso a coluna status_meta. A coincidencia entre o Cluster 3 e os usuarios com status CONCLUIDA reforca a validade do agrupamento para os clusters baseados em receita, despesa e saldo (0, 1 e 2).

Essa coincidencia especifica do Cluster 3, porem, deve ser lida com cautela: por definicao, concluir uma meta implica ter percentual_meta igual a 100%, entao essa variavel ja carregava essa informacao de forma direta. Nao se trata de uma descoberta independente do algoritmo, e sim de uma consequencia logica dos proprios dados.

Tambem vale registrar uma limitacao: a amostra e pequena (50 usuarios), e o Cluster 1 tem apenas 3 usuarios, o que fragiliza a robustez estatistica desse grupo especifico. Interpretacoes sobre esse cluster devem ser tratadas como indicativas, nao conclusivas.
