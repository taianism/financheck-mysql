import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../dados/financheck_analise.csv")

print(df.shape)
print(df.head())

colunas_cluster = ["total_receitas", "total_despesas", "saldo", "percentual_meta"]
dados_cluster = df[colunas_cluster]

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_cluster)

df_padronizado = pd.DataFrame(dados_padronizados, columns=colunas_cluster)
print(df_padronizado.describe())

df_padronizado.to_csv("../dados/financheck_padronizado.csv", index=False)
print("Arquivo padronizado salvo com sucesso.")
