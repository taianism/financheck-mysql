CREATE TABLE IF NOT EXISTS cluster_usuario (
    id_usuario INT PRIMARY KEY,
    cluster INT NOT NULL,
    total_receitas DECIMAL(10,2),
    total_despesas DECIMAL(10,2),
    saldo DECIMAL(10,2),
    percentual_meta DECIMAL(5,2),
    data_execucao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);