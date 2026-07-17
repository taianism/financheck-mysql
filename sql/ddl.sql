-- =========================================
-- LIMPEZA TOTAL DO AMBIENTE
-- =========================================
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS financheck;

SET FOREIGN_KEY_CHECKS = 1;

-- =========================================
-- CRIAÇÃO DO BANCO DE DADOS
-- =========================================
CREATE DATABASE financheck
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE financheck;

-- =========================================
-- TABELA USUARIO
-- =========================================
CREATE TABLE usuario (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(150) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_usuario PRIMARY KEY (id_usuario),
    CONSTRAINT uq_usuario_email UNIQUE (email)
) ENGINE=InnoDB;

-- =========================================
-- TABELA CATEGORIA
-- =========================================
CREATE TABLE categoria (
    id_categoria INT NOT NULL AUTO_INCREMENT,
    nome_categoria VARCHAR(100) NOT NULL,
    tipo_categoria ENUM('RECEITA','DESPESA') NOT NULL,
    descricao VARCHAR(255),

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria),
    CONSTRAINT uq_categoria_nome_tipo UNIQUE (nome_categoria, tipo_categoria)
) ENGINE=InnoDB;

-- =========================================
-- TABELA RECEITA
-- =========================================
CREATE TABLE receita (
    id_receita INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_categoria INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(12,2) NOT NULL,
    data_receita DATE NOT NULL,
    data_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_receita PRIMARY KEY (id_receita),

    CONSTRAINT fk_receita_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_receita_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================
-- TABELA DESPESA
-- =========================================
CREATE TABLE despesa (
    id_despesa INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_categoria INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(12,2) NOT NULL,
    data_despesa DATE NOT NULL,
    data_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_despesa PRIMARY KEY (id_despesa),

    CONSTRAINT fk_despesa_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_despesa_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================
-- TABELA META FINANCEIRA
-- =========================================
CREATE TABLE meta_financeira (
    id_meta INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    titulo_meta VARCHAR(150) NOT NULL,
    descricao_meta VARCHAR(255),
    valor_objetivo DECIMAL(12,2) NOT NULL,
    valor_atual DECIMAL(12,2) NOT NULL DEFAULT 0,
    data_inicio DATE NOT NULL,
    data_limite DATE NOT NULL,
    status_meta ENUM('EM_ANDAMENTO','CONCLUIDA','CANCELADA')
        NOT NULL DEFAULT 'EM_ANDAMENTO',

    CONSTRAINT pk_meta_financeira PRIMARY KEY (id_meta),

    CONSTRAINT fk_meta_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =========================================
-- ÍNDICES PARA PERFORMANCE (BI / CONSULTAS)
-- =========================================

CREATE INDEX idx_receita_data ON receita(data_receita);
CREATE INDEX idx_receita_usuario ON receita(id_usuario);
CREATE INDEX idx_receita_categoria ON receita(id_categoria);

CREATE INDEX idx_despesa_data ON despesa(data_despesa);
CREATE INDEX idx_despesa_usuario ON despesa(id_usuario);
CREATE INDEX idx_despesa_categoria ON despesa(id_categoria);

CREATE INDEX idx_meta_usuario ON meta_financeira(id_usuario);
CREATE INDEX idx_meta_data_limite ON meta_financeira(data_limite);