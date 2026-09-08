import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("../dados/financheck_com_clusters.csv")

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="financheck"
)
cursor = conexao.cursor()

sql = """
INSERT INTO cluster_usuario (id_usuario, cluster, total_receitas, total_despesas, saldo, percentual_meta)
VALUES (%s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    cluster = VALUES(cluster),
    total_receitas = VALUES(total_receitas),
    total_despesas = VALUES(total_despesas),
    saldo = VALUES(saldo),
    percentual_meta = VALUES(percentual_meta)
"""

for _, linha in df.iterrows():
    cursor.execute(sql, (
        int(linha["id_usuario"]),
        int(linha["cluster"]),
        float(linha["total_receitas"]),
        float(linha["total_despesas"]),
        float(linha["saldo"]),
        float(linha["percentual_meta"])
    ))

conexao.commit()
print(f"Total de registros inseridos/atualizados: {len(df)}")

cursor.close()
conexao.close()