CREATE VIEW vendas(ean, cat, ano, trimestre, mes, dia_mes, dia_semana, distrito, concelho, unidades) AS
SELECT ean, cat, EXTRACT(YEAR FROM instante) AS ano, EXTRACT(MONTH FROM instante) as mes,
EXTRACT(QUARTER FROM instante) AS trimestre, EXTRACT(DAY FROM instante) AS dia_mes,
EXTRACT(DOW FROM instante) AS dia_semana, distrito, concelho, unidades FROM 
produto NATURAL JOIN ponto_de_retalho NATURAL JOIN evento_reposicao;


