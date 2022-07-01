-- TABLE: categoria
-- inserir values em categoria
INSERT INTO categoria VALUES ('Doces');
INSERT INTO categoria VALUES ('Bolachas');
INSERT INTO categoria VALUES ('Chocolates');
INSERT INTO categoria VALUES ('Bombons');
INSERT INTO categoria VALUES ('Bebidas');
INSERT INTO categoria VALUES ('Refrigerantes');
INSERT INTO categoria VALUES ('Agua');
INSERT INTO categoria VALUES ('Barras');

-- TABLE: categoria_simples
-- inserir values em categoria_simples
INSERT INTO categoria_simples VALUES('Bolachas');
INSERT INTO categoria_simples VALUES('Bombons');
INSERT INTO categoria_simples VALUES('Agua');
INSERT INTO categoria_simples VALUES('Refrigerantes');
INSERT INTO categoria_simples VALUES('Barras');

-- TABLE: super_categoria
-- inserir values em super_categoria
INSERT INTO super_categoria VALUES('Doces');
INSERT INTO super_categoria VALUES('Chocolates');
INSERT INTO super_categoria VALUES('Bebidas');

-- TABLE: tem_outra
-- inserir values em tem_outra
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Doces','Chocolates');
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Chocolates','Bombons');
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Chocolates','Barras');
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Doces','Bolachas');
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Bebidas','Agua');
INSERT INTO tem_outra(super_categoria,categoria) VALUES('Bebidas','Refrigerantes');

-- TABLE: produto
-- inserir values em produto
INSERT INTO produto(ean,cat,descr) VALUES(1,'Barras','Twix');
INSERT INTO produto(ean,cat,descr) VALUES(2,'Barras','Kinder');
INSERT INTO produto(ean,cat,descr) VALUES(3,'Bombons','Brigadeiro');
INSERT INTO produto(ean,cat,descr) VALUES(4,'Bolachas','Oreo');
INSERT INTO produto(ean,cat,descr) VALUES(5,'Bolachas','Chips Ahoy');
INSERT INTO produto(ean,cat,descr) VALUES(6,'Bolachas','Nutter Butters');
INSERT INTO produto(ean,cat,descr) VALUES(7,'Agua','Agua Mineral');
INSERT INTO produto(ean,cat,descr) VALUES(8,'Refrigerantes','Sumol');
INSERT INTO produto(ean,cat,descr) VALUES(9,'Refrigerantes','Pepsi');

-- TABLE: tem_categoria
-- inserir values em tem_categoria
INSERT INTO tem_categoria(ean,nome) VALUES(1,'Barras');
INSERT INTO tem_categoria(ean,nome) VALUES(2,'Barras');
INSERT INTO tem_categoria(ean,nome) VALUES(3,'Bombons');
INSERT INTO tem_categoria(ean,nome) VALUES(4,'Bolachas');
INSERT INTO tem_categoria(ean,nome) VALUES(5,'Bolachas');
INSERT INTO tem_categoria(ean,nome) VALUES(6,'Bolachas');
INSERT INTO tem_categoria(ean,nome) VALUES(7,'Agua');
INSERT INTO tem_categoria(ean,nome) VALUES(8,'Refrigerantes');
INSERT INTO tem_categoria(ean,nome) VALUES(9,'Refrigerantes');

-- TABLE: IVM
-- inserir values em IVM
INSERT INTO IVM(num_serie,fabricante) VALUES('101','Convenience Joy');
INSERT INTO IVM(num_serie,fabricante) VALUES('102','Vibrant Vendors');
INSERT INTO IVM(num_serie,fabricante) VALUES('103','Convenience Joy');
INSERT INTO IVM(num_serie,fabricante) VALUES('104','Vibrant Vendors');
INSERT INTO IVM(num_serie,fabricante) VALUES('105','Convenience Joy');

-- TABLE: ponto_de_retalho
-- inserir values em ponto_de_retalho
INSERT INTO ponto_de_retalho(nome,distrito,concelho) VALUES('Montijo Shopping','Lisboa','Montijo');
INSERT INTO ponto_de_retalho(nome,distrito,concelho) VALUES('Vasco da Gama','Lisboa','Lisboa');
INSERT INTO ponto_de_retalho(nome,distrito,concelho) VALUES('Alegro Alfragide','Lisboa','Amadora');

-- TABLE: instalada_em
-- inserir values em instalada_em
INSERT INTO instalada_em(num_serie,fabricante,"local") VALUES('101','Convenience Joy','Montijo Shopping');
INSERT INTO instalada_em(num_serie,fabricante,"local") VALUES('102','Vibrant Vendors','Alegro Alfragide');
INSERT INTO instalada_em(num_serie,fabricante,"local") VALUES('103','Convenience Joy','Alegro Alfragide');
INSERT INTO instalada_em(num_serie,fabricante,"local") VALUES('104','Vibrant Vendors','Vasco da Gama');
INSERT INTO instalada_em(num_serie,fabricante,"local") VALUES('105','Convenience Joy','Vasco da Gama');

-- TABLE: prateleira
-- inserir values em prateleira
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1001,'101','Convenience Joy',8,'Barras');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1002,'101','Convenience Joy',7,'Bolachas');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1003,'101','Convenience Joy',8,'Bombons');

INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1004,'102','Vibrant Vendors',8,'Barras');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1005,'102','Vibrant Vendors',7,'Agua');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1006,'102','Vibrant Vendors',8,'Refrigerantes');

INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1007,'103','Convenience Joy',8,'Agua');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1008,'103','Convenience Joy',7,'Refrigerantes');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1009,'103','Convenience Joy',8,'Bombons');

INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1010,'104','Vibrant Vendors',8,'Barras');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1011,'104','Vibrant Vendors',7,'Bolachas');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1012,'104','Vibrant Vendors',8,'Refrigerantes');

INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1013,'105','Convenience Joy',8,'Agua');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1014,'105','Convenience Joy',7,'Bolachas');
INSERT INTO prateleira(nro,num_serie,fabricante,altura,nome) VALUES(1015,'105','Convenience Joy',8,'Bombons');

-- TABLE: planograma
-- inserir values em planograma
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(1,1001,'101','Convenience Joy',1,4,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(2,1001,'101','Convenience Joy',1,4,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(4,1002,'101','Convenience Joy',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(5,1002,'101','Convenience Joy',1,3,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(6,1002,'101','Convenience Joy',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(3,1003,'101','Convenience Joy',1,8,'baixo');

INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(1,1004,'102','Vibrant Vendors',1,5,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(2,1004,'102','Vibrant Vendors',1,3,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(7,1005,'102','Vibrant Vendors',1,7,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(8,1006,'102','Vibrant Vendors',1,4,'baixo');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(9,1006,'102','Vibrant Vendors',1,4,'baixo');

INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(7,1007,'103','Convenience Joy',1,8,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(8,1008,'103','Convenience Joy',1,4,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(9,1008,'103','Convenience Joy',1,3,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(3,1009,'103','Convenience Joy',1,8,'baixo');

INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(1,1010,'104','Vibrant Vendors',1,2,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(2,1010,'104','Vibrant Vendors',1,6,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(4,1011,'104','Vibrant Vendors',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(5,1011,'104','Vibrant Vendors',1,3,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(6,1011,'104','Vibrant Vendors',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(8,1012,'104','Vibrant Vendors',1,4,'baixo');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(9,1012,'104','Vibrant Vendors',1,4,'baixo');

INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(7,1013,'105','Convenience Joy',1,8,'cima');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(4,1014,'105','Convenience Joy',1,3,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(5,1014,'105','Convenience Joy',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(6,1014,'105','Convenience Joy',1,2,'meio');
INSERT INTO planograma(ean,nro,num_serie,fabricante,faces,unidades,loc) VALUES(3,1015,'105','Convenience Joy',1,8,'baixo');

-- TABLE: retalhista
-- inserir values em retalhista
INSERT INTO retalhista(tin,nome) VALUES(10001,'Replace R Us');
INSERT INTO retalhista(tin,nome) VALUES(10002,'Filler World');
INSERT INTO retalhista(tin,nome) VALUES(10003,'Retail INC');

-- TABLE: responsavel_por
-- inserir values em responsavel_por
/*
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Barras',10001,'101','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bombons',10001,'101','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bolachas',10002,'101','Convenience Joy');

INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Barras',10003,'102','Vibrant Vendors');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Agua',10001,'102','Vibrant Vendors');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Refrigerantes',10001,'102','Vibrant Vendors');

INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Agua',10002,'103','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Refrigerantes',10003,'103','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bombons',10002,'103','Convenience Joy');

INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Barras',10003,'104','Vibrant Vendors');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bolachas',10001,'104','Vibrant Vendors');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Refrigerantes',10002,'104','Vibrant Vendors');

INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Agua',10001,'105','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bolachas',10003,'105','Convenience Joy');
INSERT INTO responsavel_por(nome_cat,tin,num_serie,fabricante) VALUES('Bombons',10001,'105','Convenience Joy');
*/

-- TABLE: evento_reposicao
-- inserir values em evento_reposicao
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(1,1001,'101',
'Convenience Joy','2022-01-01',3,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(8,1012,'104',
'Vibrant Vendors','2022-01-02',1,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(1,1001,'101',
'Convenience Joy','2022-01-03',3,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(4,1011,'104',
'Vibrant Vendors','2022-01-04',1,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(5,1011,'104',
'Vibrant Vendors','2022-01-04',1,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(6,1011,'104',
'Vibrant Vendors','2022-01-04',1,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(1,1001,'101',
'Convenience Joy','2022-01-05',3,10001);
INSERT INTO evento_reposicao(ean,nro,num_serie,fabricante,instante,unidades,tin) VALUES(2,1001,'101',
'Convenience Joy','2022-01-05',3,10001);