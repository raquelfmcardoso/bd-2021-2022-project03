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
from flask import render_template, request
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

@app.route("/list_categories")
def list_categories():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM categoria_simples;"
        cursor.execute(query)
        return render_template("list_categories.html", cursor=cursor)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        dbConn.close()

@app.route("/add_remove", methods=["POST"])
def update_balance():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        balance = request.form["balance"]
        account_number = request.form["account_number"]
        query = "UPDATE account SET balance=%s WHERE account_number = %s"
        data = (balance, account_number)
        cursor.execute(query, data)
        return query
    except Exception as e:
        return str(e)
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

if __name__ == "__main__":
    app.run(debug=True)
