import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/financheck_analise.csv")
colunas_cluster = ["total_receitas", "total_despesas", "saldo", "percentual_meta"]
dados_cluster = df[colunas_cluster]

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_cluster)

inercias = []
silhouettes = []
valores_k = range(2, 11)

for k in valores_k:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(dados_padronizados)
    inercias.append(kmeans.inertia_)
    silhouettes.append(silhouette_score(dados_padronizados, labels))
    print(f"K={k}  inercia={kmeans.inertia_:.2f}  silhouette={silhouettes[-1]:.4f}")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(valores_k, inercias, marker="o")
plt.xlabel("Numero de clusters (K)")
plt.ylabel("Inercia")
plt.title("Metodo do Cotovelo")

plt.subplot(1, 2, 2)
plt.plot(valores_k, silhouettes, marker="o", color="orange")
plt.xlabel("Numero de clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")

plt.tight_layout()
plt.savefig("../dados/escolha_k.png")
print("Grafico salvo em dados/escolha_k.png")