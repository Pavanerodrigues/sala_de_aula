CREATE TABLE IF NOT EXISTS cliente (
	id_cliente SERIAL PRIMARY KEY, 
	nome VARCHAR(100)NOT NULL,
	telefone VARCHAR(20)NOT NULL, 
	email VARCHAR(120), 
	tipo VARCHAR (50)
);

CREATE TABLE IF NOT EXISTS encomenda (
    id_encomenda SERIAL PRIMARY KEY, 
	data_pedido DATE, 
	data_pagamento DATE, 
	data_retirada DATE, 
	descricao TEXT 
); 

CREATE TABLE IF NOT EXISTS item_encomenda (
	quantidade INTEGER, 
	preco NUMERIC(10,2)
);

CREATE TYPE tipo_produto as ENUM ('caneca','camiseta');

CREATE TABLE IF NOT EXISTS produto (
    id_produto SERIAL PRIMARY KEY,
    tipo tipo_produto,
    preco NUMERIC(10,2),
    quantidade_disponivel INTEGER
);




