import mysql.connector
from flask import Flask, render_template, make_response, jsonify, request


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_urls',
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # Ordena de A-Z quando é TRUE

def links():
    return render_template('links.html')


@app.route('/urls', methods=['GET'])  
def get_urls():

    # CURSOR é como se fosse um agente que vai executar o código sql que for passado para ele no banco de dados 
    # e através dele é capaz de obter algumas funções para manipular os dados
    my_cursor = mydb.cursor() 
    
    # ele carregou dentro do cursor todos os dados que ele capturou do SELECT
    my_cursor.execute('SELECT * FROM urls') 
    
    # fetchall retorna a lista de todos os dados que ele conseguiu capturar com o SQL 
    # e estou atribuindo a lista de todos esses dados a uma variável (meus_carros)
    minhas_urls = my_cursor.fetchall() 

    urls = list()
    for url in minhas_urls:
        urls.append(
            {
                'id': url[0],
                'link': url[1],
                'titulo': url[2],
            }
        )

    return make_response(
        jsonify(
            mensagem='Lista de urls',
            dados=urls
        )
    )


@app.route('/urls', methods=['POST'])
def create_url():
    url = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO urls (link, titulo) VALUES ('{url['link']}', '{url['titulo']}" 
    my_cursor.execute(sql) # executa e insere os dados que você quer
    mydb.commit() # registrar a transação no banco de dados

    return make_response(
        jsonify(
            mensagem='URL cadastrada com sucesso!',
            url=url
        )
    )

@app.route('/urls', methods=['DELETE'])
def create_url():
    url = request.json

    my_cursor = mydb.cursor()
    sql_delete = f'DELETE FROM urls WHERE link = "{id}"'
    my_cursor.execute(sql_delete) # executa e deleta os dados que você quer
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='URL deletada com sucesso!',
            url=url
        )
    )

app.run()
