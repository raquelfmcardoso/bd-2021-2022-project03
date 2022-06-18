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
DB_USER = myuser
DB_DATABASE = DB_USER
DB_PASSWORD = hunter2
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (
    DB_HOST,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
)

app = Flask(__name__)


