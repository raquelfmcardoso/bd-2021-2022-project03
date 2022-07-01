CREATE OR REPLACE FUNCTION check_category()
RETURNS TRIGGER AS 
$$
BEGIN
  IF NEW.categoria = NEW.super_categoria THEN
    RAISE EXCEPTION 'Uma categoria nao pode estar contida nela propria';
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_check_category
BEFORE UPDATE OR INSERT ON tem_outra
FOR EACH ROW EXECUTE PROCEDURE check_category();


------------------------------------------------
CREATE OR REPLACE FUNCTION check_unidades()
RETURNS TRIGGER AS 
$$
BEGIN
  IF NOT EXISTS (SELECT FROM planograma WHERE (NEW.nro = planograma.nro AND NEW.num_serie = planograma.num_serie
    AND NEW.ean = planograma.ean AND NEW.unidades <= planograma.unidades)) THEN
    RAISE EXCEPTION 'O numero de unidades repostas num evento de reposicao nao pode exceder o numero de unidades especificadas
    pelo planograma';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_check_unidades
BEFORE UPDATE OR INSERT ON evento_reposicao
FOR EACH ROW EXECUTE PROCEDURE check_unidades();

-----------------------------------------

CREATE OR REPLACE FUNCTION check_cat_prateleira()
RETURNS TRIGGER AS 
$$
BEGIN
  IF NOT EXISTS (SELECT ean FROM produto WHERE (produto.cat IN(SELECT nome FROM 
    prateleira WHERE NEW.nro = prateleira.nro) AND NEW.ean = produto.ean)) THEN
    RAISE EXCEPTION 'Um produto so pode ser reposto numa prateleira que apresente uma das categorias desse produto';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_check_cat_prateleira
BEFORE UPDATE OR INSERT ON evento_reposicao
FOR EACH ROW EXECUTE PROCEDURE check_cat_prateleira();

