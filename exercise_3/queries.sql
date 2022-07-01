-- EX 1
SELECT nome FROM retalhista WHERE retalhista.tin IN (
    SELECT tin, COUNT(DISTINCT nome_cat) FROM responsavel_por GROUP BY tin
    HAVING COUNT(DISTINCT nome_cat) >= ALL(
        SELECT COUNT(DISTINCT nome_cat) FROM responsavel_por GROUP BY tin
    )
);

-- EX 2
SELECT nome FROM retalhista NATURAL JOIN responsavel_por WHERE responsavel_por.nome_cat IN 
(SELECT nome FROM categoria_simples )
GROUP BY tin HAVING COUNT(*) = (SELECT COUNT(*) FROM categoria_simples);

-- EX 3
SELECT ean FROM produto WHERE produto.ean NOT IN(SELECT ean FROM evento_reposicao);

-- EX 4
SELECT ean FROM produto WHERE produto.ean IN(SELECT ean FROM(
    SELECT a.* FROM evento_reposicao a INNER JOIN(SELECT ean, fabricante, COUNT(*)
totalCOUNT FROM evento_reposicao GROUP BY ean,fabricante HAVING COUNT(*) > 1)
b ON a.fabricante = b.fabricante AND a.ean = b.ean) AS ean);



