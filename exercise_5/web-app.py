'''
Crie um protótipo de aplicação web em scripts Python CGI e páginas HTML que permita:
a) Inserir e remover categorias e sub-categorias;
b) Inserir e remover um retalhista, com todos os seus produtos, garantindo que esta operação seja
atómica;
c) Listar todos os eventos de reposição de uma IVM, apresentando o número de unidades repostas por
categoria de produto;
d) Listar todas as sub-categorias de uma super-categoria, a todos os níveis de profundidade.
A solução deve prezar pela segurança, prevenindo ataques por SQL INJECTION. Além disso, a atomicidade
das operações sobre a base de dados deve estar assegurada. Pode-se utilizar CSS, embora não seja objeto
de avaliação.

A solução deve prezar pela segurança, prevenindo ataques por SQL INJECTION.
Além disso, a atomicidade das operações sobre a base de dados deve estar assegurada.
Pode-se utilizar CSS, embora não seja objeto de avaliação.
'''

#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect, url_for

import psycopg2
import psycopg2.extras

## SGBD configs
DB_HOST = "db.tecnico.ulisboa.pt"
DB_USER = "ist199287"
DB_DATABASE = DB_USER
DB_PASSWORD = "Miguel2003"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (
    DB_HOST,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/retailers")
def retailers():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM retalhista;"
        cursor.execute(query)
        return render_template("retailers.html", cursor=cursor, params=request.args)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        dbConn.close()

@app.route('/retailers/add')
def add_retailer():
  try:
    return render_template("add_retailer.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/retailers/adding', methods=["POST"])
def adding_retailer_database():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO retalhista VALUES (%s,%s);"
    data = (request.form["tin"], request.form["nome"])
    cursor.execute(query,data)
    return redirect(url_for('retailers'))
  except Exception as e:
    #return redirect(url_for('erro'))
    return str(e)
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/retailers/remove')
def add_retailer():
  try:
    return render_template("remove_retailer.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route("/retailers/removing", methods=["POST"])
def removing_retailer_database():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM retalhista WHERE tin=%s;" #falta tirar o produto e wtv
    data = (request.form["tin"])
    cursor.execute(query,data)
    return redirect(url_for('retailers'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()
