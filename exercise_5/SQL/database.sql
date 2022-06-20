DROP TABLE IF EXISTS categoria CASCADE;
DROP TABLE IF EXISTS categoria_simples CASCADE;
DROP TABLE IF EXISTS super_categoria CASCADE;
DROP TABLE IF EXISTS tem_outra CASCADE;
DROP TABLE IF EXISTS produto CASCADE;
DROP TABLE IF EXISTS tem_categoria CASCADE;
DROP TABLE IF EXISTS IVM CASCADE;
DROP TABLE IF EXISTS ponto_de_retalho CASCADE;
DROP TABLE IF EXISTS instalada_em CASCADE;
DROP TABLE IF EXISTS prateleira CASCADE;
DROP TABLE IF EXISTS planograma CASCADE;
DROP TABLE IF EXISTS retalhista CASCADE;
DROP TABLE IF EXISTS responsavel_por CASCADE;
DROP TABLE IF EXISTS evento_reposicao CASCADE;


CREATE TABLE categoria(
nome VARCHAR(40) NOT NULL,
CONSTRAINT pk_categoria PRIMARY KEY(nome)
);

CREATE TABLE categoria_simples(
nome VARCHAR(40) NOT NULL,
CONSTRAINT pk_categoria_simples PRIMARY KEY(nome),
CONSTRAINT fk_categoria_simples FOREIGN KEY(nome) REFERENCES categoria(nome) 
);

CREATE TABLE super_categoria(
nome VARCHAR(40) NOT NULL,
CONSTRAINT pk_super_categoria PRIMARY KEY(nome),
CONSTRAINT fk_super_categoria FOREIGN KEY(nome) REFERENCES categoria(nome)
);

CREATE TABLE tem_outra(
super_categoria VARCHAR(40) NOT NULL,
categoria VARCHAR(40) NOT NULL,
CONSTRAINT pk_tem_outra PRIMARY KEY(categoria),
CONSTRAINT fk1_tem_outra FOREIGN KEY(super_categoria) REFERENCES super_categoria(nome),
CONSTRAINT fk2_tem_outra FOREIGN KEY(categoria) REFERENCES categoria(nome)
);

CREATE TABLE produto(
ean INT NOT NULL,
cat VARCHAR(40) NOT NULL,
descr VARCHAR(40) NOT NULL,
CONSTRAINT pk_produto PRIMARY KEY(ean),
CONSTRAINT fk_produto FOREIGN KEY(cat) REFERENCES categoria(nome)
);

CREATE TABLE tem_categoria(
ean INT NOT NULL,
nome VARCHAR(40) NOT NULL,
CONSTRAINT fk1_tem_categoria FOREIGN KEY(ean) REFERENCES produto(ean),
CONSTRAINT fk2_tem_categoria FOREIGN KEY(nome) REFERENCES categoria(nome)
);

CREATE TABLE IVM(
num_serie CHAR(20) NOT NULL  ,
fabricante VARCHAR(40) NOT NULL ,
CONSTRAINT pk_IVM PRIMARY KEY(num_serie,fabricante)
);

CREATE TABLE ponto_de_retalho(
nome VARCHAR(40) NOT NULL ,
distrito VARCHAR(40) NOT NULL,
concelho VARCHAR(40) NOT NULL,
CONSTRAINT pk_ponto_de_retalho PRIMARY KEY(nome) 
);

CREATE TABLE instalada_em(
num_serie CHAR(20) NOT NULL ,
fabricante VARCHAR(40) NOT NULL ,
local VARCHAR(40) NOT NULL ,
CONSTRAINT pk_instalada_em PRIMARY KEY(num_serie,fabricante),
CONSTRAINT fk1_instalada_em FOREIGN KEY(num_serie,fabricante) REFERENCES IVM(num_serie,fabricante),
CONSTRAINT fk2_instalada_em FOREIGN KEY(local) REFERENCES ponto_de_retalho(nome)
);

CREATE TABLE prateleira(
nro INT NOT NULL ,
num_serie CHAR(20) NOT NULL ,
fabricante VARCHAR(40) NOT NULL ,
altura INT NOT NULL,
nome VARCHAR(40) NOT NULL,
CONSTRAINT pk_prateleira PRIMARY KEY(nro,num_serie,fabricante),
CONSTRAINT fk1_prateleira FOREIGN KEY(num_serie,fabricante) REFERENCES IVM(num_serie,fabricante),
CONSTRAINT fk2_prateleira FOREIGN KEY(nome) REFERENCES categoria(nome)
);

CREATE TABLE planograma(
ean INT NOT NULL,
nro INT NOT NULL ,
num_serie CHAR(20) NOT NULL ,
fabricante VARCHAR(40) NOT NULL ,
faces INT NOT NULL,
unidades INT NOT NULL,
loc VARCHAR(40) NOT NULL,
CONSTRAINT pk_planograma PRIMARY KEY(ean,nro,num_serie,fabricante),
CONSTRAINT fk1_planograma FOREIGN KEY(ean) REFERENCES produto(ean),
CONSTRAINT fk2_planograma FOREIGN KEY(num_serie,fabricante,nro) REFERENCES prateleira(num_serie,fabricante,nro)
);

CREATE TABLE retalhista(
tin INT NOT NULL,
nome VARCHAR(40) NOT NULL, 
CONSTRAINT pk_retalhista PRIMARY KEY(tin)
);

CREATE TABLE responsavel_por(
nome_cat VARCHAR(40) NOT NULL,
tin INT NOT NULL,
num_serie CHAR(20) NOT NULL ,
fabricante VARCHAR(40) NOT NULL ,
CONSTRAINT pk_responsavel_por PRIMARY KEY(num_serie,fabricante),
CONSTRAINT fk1_responsavel_por FOREIGN KEY(num_serie,fabricante) REFERENCES IVM(num_serie,fabricante),
CONSTRAINT fk2_responsavel_por FOREIGN KEY(tin) REFERENCES retalhista(tin),
CONSTRAINT fk3_responsavel_por FOREIGN KEY(nome_cat) REFERENCES categoria(nome)
);

CREATE TABLE evento_reposicao(
ean INT NOT NULL,
nro INT NOT NULL ,
tin INT NOT NULL,
num_serie CHAR(20) NOT NULL,
fabricante VARCHAR(40) NOT NULL,
instante DATE NOT NULL,
unidades INT NOT NULL,
CONSTRAINT pk_evento_reposicao PRIMARY KEY(ean,nro,num_serie,fabricante,instante),
CONSTRAINT fk1_evento_reposicao FOREIGN KEY(ean,nro,num_serie,fabricante) REFERENCES planograma(ean,nro,num_serie,fabricante),
CONSTRAINT fk2_evento_reposicao FOREIGN KEY(tin) REFERENCES retalhista(tin)
);