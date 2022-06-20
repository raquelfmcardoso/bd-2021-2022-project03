#!/usr/bin/python3

from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect, url_for

## Libs postgres
import psycopg2
import psycopg2.extras

app = Flask(__name__)

## SGBD configs
DB_HOST="db.tecnico.ulisboa.pt"
DB_USER="ist189508" 
DB_DATABASE=DB_USER
DB_PASSWORD="LARILINDA"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)


## Runs the function once the root page is requested.
## The request comes with the folder structure setting ~/web as the root
@app.route('/')
def index():
  try:
    return render_template("index.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/menu')
def menu_principal():
  try:
    return render_template("index.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/erro')
def erro():
  try:
    return render_template("erro.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicoes')
def editar_instituicoes():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT i.nome, i.tipo, i.num_regiao, i.num_concelho, c.nome FROM instituicao as i,concelho as c WHERE i.num_regiao=c.num_regiao AND i.num_concelho=c.num_concelho;"
    cursor.execute(query)
    return render_template("instituicoes.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/medicos')
def editar_medicos():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM medico;"
    cursor.execute(query)
    return render_template("medicos.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()


@app.route('/prescricoes')
def editar_prescricoes():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao;"
    cursor.execute(query)
    return render_template("prescricoes.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/analises')
def editar_analises():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM analise;"
    cursor.execute(query)
    return render_template("analises.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/vendas')
def editar_vendas():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM venda_farmacia;"
    cursor.execute(query)
    return render_template("vendas.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/substancias_medico')
def substancias_medico_request():
  try:
    return render_template("listar_substancias.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicoes/inserir_request')
def inserir_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM concelho;"
    cursor.execute(query)
    return render_template("inserir_instituicao.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/medicos/inserir_form')
def inserir_medico():
  try:
    return render_template("inserir_medico.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/prescricoes/inserir_form')
def inserir_prescricao():
  try:
    return render_template("inserir_prescricao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/analises/inserir_form')
def inserir_analise():
  try:
    return render_template("inserir_analise.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/vendas/inserir_com_prescricao_form')
def inserir_venda_com_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT nome FROM instituicao WHERE tipo='farmacia';"
    cursor.execute(query)
    return render_template("inserir_venda_com_prescricao.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/vendas/inserir_sem_prescricao_form')
def inserir_venda_sem_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT nome FROM instituicao WHERE tipo='farmacia';"
    cursor.execute(query)
    return render_template("inserir_venda_sem_prescricao.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) 
  finally:
    cursor.close()
    dbConn.close()

@app.route('/instituicoes/alterar')
def alterar_instituicao():
  try:
    return render_template("alterar_instituicao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/medicos/alterar')
def alterar_medico():
  try:
    return render_template("alterar_medico.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/prescricoes/alterar')
def alterar_prescricao():
  try:
    return render_template("alterar_prescricao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/analises/alterar')
def alterar_analise():
  try:
    return render_template("alterar_analise.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/vendas/alterar')
def alterar_venda():
  try:
    return render_template("alterar_venda.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicoes/remover')
def remover_instituicao():
  try:
    return render_template("remover_instituicao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/medicos/remover')
def remover_medico():
  try:
    return render_template("remover_medico.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/prescricoes/remover')
def remover_prescricao():
  try:
    return render_template("remover_prescricao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/analises/remover')
def remover_analise():
  try:
    return render_template("remover_analise.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/vendas/remover')
def remover_venda():
  try:
    return render_template("remover_venda.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/instituicoes/perform_delete', methods=["POST"])
def delete_instituicao_fromDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM instituicao WHERE nome=%s;"
    data = (request.form["nome"],)
    cursor.execute(query,data)
    return redirect(url_for('editar_instituicoes'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/medicos/perform_delete', methods=["POST"])
def delete_medico_fromDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM medico WHERE num_cedula=%s;"
    data = (request.form["num_cedula"])
    cursor.execute(query,data)
    return redirect(url_for('editar_medicos'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/prescricoes/perform_delete', methods=["POST"])
def delete_prescricao_fromDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM prescricao WHERE num_cedula=%s AND num_doente=%s AND data_hora=%s AND substancia=%s;"
    data = (request.form["num_cedula_original"],request.form["num_doente_original"], request.form["data_original"], request.form["substancia_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_prescricoes'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/analises/perform_delete', methods=["POST"])
def delete_analise_fromDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM analise WHERE num_analise=%s;"
    data = (request.form["num_analise"],)
    cursor.execute(query,data)
    return redirect(url_for('editar_analises'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/vendas/perform_delete', methods=["POST"])
def delete_venda_fromDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM venda_farmacia WHERE num_venda=%s;"
    data = (request.form["num_venda"],)
    cursor.execute(query,data)
    return redirect(url_for('editar_vendas'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/instituicoes/execute_insert', methods=["POST"])
def insert_institution_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO instituicao VALUES (%s,%s,%s,%s);"
    data = (request.form["nome"],request.form["tipo"],request.form["num_regiao"],request.form["num_concelho"],)
    cursor.execute(query,data)
    return redirect(url_for('editar_instituicoes'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/medicos/execute_insert', methods=["POST"])
def insert_doctor_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO medico VALUES (%s,%s,%s);"
    data = (request.form["num_cedula"],request.form["nome"],request.form["especialidade"])
    cursor.execute(query,data)
    return redirect(url_for('editar_medicos'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/prescricoes/execute_insert', methods=["POST"])
def insert_prescricao_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO prescricao VALUES (%s,%s,%s,%s,%s);"
    data = (request.form["num_cedula"],request.form["num_doente"],request.form["data"],request.form["substancia"],request.form["quantidade"])
    cursor.execute(query,data)
    return redirect(url_for('editar_prescricoes'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/analises/execute_insert', methods=["POST"])
def insert_analise_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    if (request.form["num_cedula"]=="" or request.form["num_doente"]==""):
      query= "INSERT INTO analise(especialidade,data_registo,nome,quantidade,inst) VALUES (%s,%s,%s,%s,%s);"
      data = (request.form["espec"],request.form["data_registo"],request.form["nome"],request.form["quant"],request.form["inst"])
    else:
      query = "INSERT INTO analise VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s);"
      data = (request.form["espec"],request.form["num_cedula"],request.form["num_doente"],request.form["data"],request.form["data_registo"],request.form["nome"],request.form["quant"],request.form["inst"])
    cursor.execute(query,data)
    return redirect(url_for('editar_analises'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/vendas/execute_insert', methods=["POST"])
def insert_venda_sem_presc_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO venda_farmacia VALUES (DEFAULT,%s,%s,%s,%s,%s);"
    data = (request.form["data_registo"],request.form["substancia"],request.form["quantidade"],request.form["preco"],request.form["inst"])
    cursor.execute(query,data)
    return redirect(url_for('editar_vendas'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/vendas/execute_insert_complex', methods=["POST"])
def insert_venda_com_presc_intoDB():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO venda_farmacia VALUES (%s,%s,%s,%s,%s,%s);"
    data = (request.form["num_venda"],request.form["data_registo"],request.form["substancia"],request.form["quantidade"],request.form["preco"],request.form["inst"])
    cursor.execute(query,data)
    try:
      query = "INSERT INTO prescricao_venda VALUES (%s,%s,%s,%s,%s);"
      data = (request.form["num_cedula"],request.form["num_doente"],request.form["data_consulta"],request.form["substancia"],request.form["num_venda"])
      cursor.execute(query,data)
      dbConn.commit()
      return redirect(url_for('editar_vendas'))
    except Exception as e:
      return redirect(url_for('erro'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    cursor.close()
    dbConn.close()

@app.route('/instituicoes/update', methods=["POST"])
def update_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "UPDATE instituicao SET nome=%s,tipo=%s,num_regiao=%s,num_concelho=%s WHERE nome = %s;"
    data = (request.form["nome"],request.form["tipo"],request.form["num_regiao"],request.form["num_concelho"],request.form["nome_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_instituicoes'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/medicos/update', methods=["POST"])
def update_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "UPDATE medico SET num_cedula=%s,nome=%s,especialidade=%s WHERE num_cedula = %s;"
    data = (request.form["num_cedula"],request.form["nome"],request.form["especialidade"],request.form["num_cedula_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_medicos'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/prescricoes/update', methods=["POST"])
def update_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "UPDATE prescricao SET num_cedula=%s, num_doente=%s, data_hora=%s, substancia=%s,quantidade=%s WHERE num_cedula=%s AND num_doente=%s AND data_hora=%s AND substancia=%s;"
    data = (request.form["num_cedula"], request.form["num_doente"], request.form["data"], request.form["substancia"],request.form["quantidade"], request.form["num_cedula_original"], request.form["num_doente_original"], request.form["data_original"], request.form["substancia_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_prescricoes'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/analises/update', methods=["POST"])
def update_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "UPDATE analise SET num_analise=%s,especialidade=%s,num_cedula=%s,num_doente=%s,data_hora=%s,data_registo=%s,nome=%s,quantidade=%s,inst=%s WHERE num_analise=%s;"
    data = (request.form["num_analise"],request.form["espec"],request.form["num_cedula"],request.form["num_doente"],request.form["data"],request.form["data_registo"],request.form["nome"],request.form["quant"],request.form["inst"],request.form["num_analise_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_analises'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/vendas/update', methods=["POST"])
def update_venda():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "UPDATE venda_farmacia SET num_venda=%s,data_registo=%s,substancia=%s,quantidade=%s,preco=%s,inst=%s WHERE num_venda=%s;"
    data = (request.form["num_venda"],request.form["data_registo"],request.form["substancia"],request.form["quantidade"],request.form["preco"],request.form["inst"], request.form["num_venda_original"])
    cursor.execute(query,data)
    return redirect(url_for('editar_vendas'))
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/listar_substancias', methods=["POST"])
def list_substancias():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao WHERE prescricao.num_cedula=%s AND EXTRACT(month from TO_DATE(%s,'YYYY-MM'))=EXTRACT(month from prescricao.data_hora);"
    data = (request.form["num_cedula"],request.form["data"])
    cursor.execute(query,data)
    return render_template("substancias_medico_mes.html", cursor=cursor, params=request.args)
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    cursor.close()
    dbConn.close()

@app.route('/glicemia')
def list_glicemia():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query =  "SELECT * FROM(SELECT B.num_doente, D.maximo, D.nome from(SELECT MAX(quantidade) as maximo, nome FROM (SELECT a.num_doente, a.quantidade, c.nome  FROM analise as a,instituicao as i, concelho as c WHERE a.nome='Glicémia' AND a.inst=i.nome AND i.num_concelho=c.num_concelho and i.num_regiao=c.num_regiao) AS T GROUP BY T.nome) as D, (SELECT a.num_doente, a.quantidade, c.nome  FROM analise as a,instituicao as i, concelho as c WHERE a.nome='Glicémia' AND a.inst=i.nome AND i.num_concelho=c.num_concelho and i.num_regiao=c.num_regiao) AS B WHERE D.maximo=B.quantidade AND D.nome=B.nome) as J,(SELECT B.num_doente, D.minimo, D.nome from(SELECT MIN(quantidade) as minimo, nome FROM (SELECT a.num_doente, a.quantidade, c.nome  FROM analise as a,instituicao as i, concelho as c WHERE a.nome='Glicémia' AND a.inst=i.nome AND i.num_concelho=c.num_concelho and i.num_regiao=c.num_regiao) AS T GROUP BY T.nome) as D, (SELECT a.num_doente, a.quantidade, c.nome  FROM analise as a,instituicao as i, concelho as c WHERE a.nome='Glicémia' AND a.inst=i.nome AND i.num_concelho=c.num_concelho and i.num_regiao=c.num_regiao) AS B WHERE D.minimo=B.quantidade AND D.nome=B.nome) as M WHERE J.nome = M.nome;"
    cursor.execute(query)
    return render_template("glicemia.html", cursor=cursor, params=request.args)
  except Exception as e:
    return redirect(url_for('erro'))
  finally:
    cursor.close()
    dbConn.close()


CGIHandler().run(app)

