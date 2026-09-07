import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/financheck_analise.csv")
colunas_cluster = ["total_receitas", "total_despesas", "saldo", "percentual_meta"]
dados_cluster = df[colunas_cluster]

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_cluster)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(dados_padronizados)

pca = PCA(n_components=2, random_state=42)
componentes = pca.fit_transform(dados_padronizados)
df["pca1"] = componentes[:, 0]
df["pca2"] = componentes[:, 1]

variancia_explicada = pca.explained_variance_ratio_
print(f"Variancia explicada pelo PCA: {variancia_explicada[0]:.2%} + {variancia_explicada[1]:.2%} = {sum(variancia_explicada):.2%}")

plt.figure(figsize=(8, 6))
cores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
for c in sorted(df["cluster"].unique()):
    subconjunto = df[df["cluster"] == c]
    plt.scatter(subconjunto["pca1"], subconjunto["pca2"], label=f"Cluster {c}", color=cores[c], s=80, edgecolor="black")

plt.xlabel(f"Componente Principal 1 ({variancia_explicada[0]:.1%} da variancia)")
plt.ylabel(f"Componente Principal 2 ({variancia_explicada[1]:.1%} da variancia)")
plt.title("Visualizacao dos Clusters FinanCheck (K=4) via PCA")
plt.legend()
plt.tight_layout()
plt.savefig("../dados/visualizacao_clusters.png")
print("Grafico salvo em dados/visualizacao_clusters.png")