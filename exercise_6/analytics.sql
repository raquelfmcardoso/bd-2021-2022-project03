-- EX 1

SELECT dia_semana, concelho, SUM(unidades) as TOTAL FROM vendas WHERE (ano == 2022) GROUPING SET(concelho, dia_semana);

-- EX 2

SELECT concelho, cat AS categoria, dia_semana, SUM(unidades) as TOTAL
 FROM vendas WHERE(vendas.distrito = 'Lisboa') GROUPING SET(concelho, cat, dia_semana);