#!/usr/bin/python3
from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect
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

@app.route('/')
def index():
    try:

        return render_template("index.html", params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.

# --------------------------------------------------- CATEGORIES ---------------------------------------------------

@app.route('/categories')
def list_categories():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM categoria;"
        cursor.execute(query)
        return render_template("categories.html", cursor=cursor, params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()

@app.route('/categories/add')
def add_category():
    try:
        return render_template("add_category.html", params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/categories/remove')
def remove_category():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM categoria;"
        cursor.execute(query)
        return render_template("remove_category.html", params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/categories/do_add', methods=["POST"])
def add_category_to_database():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "INSERT INTO categoria values(%s); INSERT INTO categoria_simples values(%s);"
        data = (request.form["nome"], request.form["nome"])
        cursor.execute(query, data)
        return redirect("/")
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

@app.route('/categories/do_remove', methods=["POST"])
def remove_category_from_database():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "DELETE FROM categoria_simples WHERE nome=%s; DELETE FROM tem_outra WHERE categoria=%s; \
            DELETE FROM produto WHERE cat=%s; DELETE FROM tem_categoria WHERE nome=%s; DELETE FROM prateleira WHERE nome=%s; \
            DELETE FROM responsavel_por WHERE nome_cat=%s; DELETE FROM tem_categoria WHERE nome=%s;\
            DELETE FROM categoria WHERE nome=%s; "
        data = (request.form["nome"], request.form["nome"], request.form["nome"], request.form["nome"],\
                request.form["nome"], request.form["nome"], request.form["nome"], request.form["nome"])
        cursor.execute(query, data)
        return redirect("/")
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

# --------------------------------------------------- RETAILERS ---------------------------------------------------

@app.route('/retailers')
def list_retailers():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM retalhista;"
        cursor.execute(query)
        return render_template("retailers.html", cursor=cursor, params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()

@app.route('/retailers/add')
def add_retailer():
  try:
    return render_template("add_retailer.html", params=request.args)
  except Exception as e:
    return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/retailers/remove')
def remove_retailer():
  try:
    return render_template("remove_retailer.html", params=request.args)
  except Exception as e:
    return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/retailers/do_add', methods=["POST"])
def add_retailer_to_database():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "INSERT INTO retalhista VALUES (%s, %s);"
    data = (request.form["tin"], request.form["nome"])
    cursor.execute(query, data)
    return redirect("/")
  except Exception as e:
    return render_template("error.html", error_message=e)  # Renders a page with the error.
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/retailers/do_remove', methods=["POST"])
def remove_retailer_from_database():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "DELETE FROM retalhista WHERE tin=%s; DELETE FROM responsavel_por WHERE tin=%s; \
        DELETE FROM evento_reposicao WHERE tin=%s;"
    data = (request.form["tin"], request.form["tin"], request.form["tin"])
    cursor.execute(query, data)
    return redirect("/")
  except Exception as e:
    return render_template("error.html", error_message=e)  # Renders a page with the error.
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

# --------------------------------------------------- REPOSITION EVENTS ---------------------------------------------------

@app.route('/reposition_events')
def list_reposition_events():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM evento_reposicao;"
        cursor.execute(query)
        return render_template("reposition_events.html", cursor=cursor, params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()

@app.route('/reposition_events/select_IVM')
def select_IVM():
    try:
        return render_template("select_ivm.html", params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/reposition_events/specific_ivm', methods = ["POST"])
def show_specific_IVM():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    query = "SELECT ean, nro, tin, num_serie, fabricante, instante, unidades, SUM(unidades), cat\
                FROM evento_reposicao NATURAL JOIN produto NATURAL JOIN ivm\
                WHERE (evento_reposicao.num_serie = '101')\
                GROUP BY evento_reposicao.ean, nro, tin, evento_reposicao.num_serie,\
                    evento_reposicao.fabricante, instante, unidades, produto.cat, sum_cat;"

    data = (request.form["num_serie"], request.form["fabricante"])
    cursor.execute(query, data)
    return render_template("specific_ivm.html", cursor=cursor, params=request.args)
  except Exception as e:
    return render_template("error.html", error_message=e)  # Renders a page with the error.
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

# --------------------------------------------------- HIERARCHY ---------------------------------------------------

@app.route('/hierarchy')
def list_hierarchy():
    dbConn = None
    cursor = None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM tem_outra;"
        cursor.execute(query)
        return render_template("hierarchy.html", cursor=cursor)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        cursor.close()
        dbConn.close()

@app.route('/hierarchy/select_super_category')
def select_super_category():
    try:
        return render_template("select_super_category.html", params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.

@app.route('/hierarchy/specific_hierarchy', methods = ["POST"])
def list_specific_hierarchy():
    dbConn=None
    cursor=None
    try:
        dbConn = psycopg2.connect(DB_CONNECTION_STRING)
        cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        query = "WITH RECURSIVE recur AS (\
                    SELECT tabela.super_categoria, tabela.categoria FROM tem_outra tabela \
                    WHERE tabela.super_categoria=%s UNION ALL\
                    SELECT tabela2.super_categoria, tabela2.categoria FROM tem_outra tabela2\
                    JOIN recur recur2 ON recur2.categoria = tabela2.super_categoria\
                ) SELECT * FROM recur;" % str("'" + request.form["nome"] + "'")
        cursor.execute(query)
        return render_template("specific_hierarchy.html", cursor=cursor, params=request.args)
    except Exception as e:
        return render_template("error.html", error_message=e)  # Renders a page with the error.
    finally:
        dbConn.commit()
        cursor.close()
        dbConn.close()

CGIHandler().run(app)

if __name__ == '__main__':
    app.run();