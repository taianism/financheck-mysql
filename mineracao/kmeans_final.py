import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("../dados/financheck_analise.csv")
colunas_cluster = ["total_receitas", "total_despesas", "saldo", "percentual_meta"]
dados_cluster = df[colunas_cluster]

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_cluster)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(dados_padronizados)

print(df["cluster"].value_counts().sort_index())
print()

print("Media das variaveis por cluster:")
print(df.groupby("cluster")[colunas_cluster].mean())
print()

print("Distribuicao de status_meta por cluster:")
print(pd.crosstab(df["cluster"], df["status_meta"]))

df.to_csv("../dados/financheck_com_clusters.csv", index=False)
print()
print("Arquivo salvo em dados/financheck_com_clusters.csv")