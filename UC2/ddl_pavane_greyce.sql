CREATE TABLE IF NOT EXISTS cliente (
	id_cliente SERIAL PRIMARY KEY, 
	nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(20) UNIQUE NOT NULL, 
	email VARCHAR(120) UNIQUE, 
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

ALTER TABLE encomenda
    ADD COLUMN IF NOT EXISTS id_cliente INTEGER;
	
ALTER TABLE encomenda
	ADD CONSTRAINT fk_id_cliente
	    FOREIGN KEY (id_cliente)
		REFERENCES cliente(id_cliente);


ALTER TABLE item_encomenda
    ADD COLUMN IF NOT EXISTS id_produto INTEGER,
    ADD COLUMN IF NOT EXISTS id_encomenda INTEGER;

ALTER TABLE item_encomenda
	ADD CONSTRAINT fk_id_produto
	    FOREIGN KEY (id_produto)
	    REFERENCES produto(id_produto);

ALTER TABLE item_encomenda
	ADD CONSTRAINT fk_id_encomenda
	    FOREIGN KEY (id_encomenda)
		REFERENCES encomenda(id_encomenda);

ALTER TABLE cliente
	ADD	UNIQUE(email);

ALTER TABLE cliente
	ADD	UNIQUE(telefone);

