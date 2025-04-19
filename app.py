from flask import Flask, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://csspclaudio:clnzEcsY8xmMVXMr@cluster0.kfgkjua.mongodb.net/')
db = client['TestsDb']

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    data = []
    if request.method == 'POST':
        # Quando for um POST (importação de arquivo)
        if 'json_file' in request.files:
            arquivo = request.files['json_file']
            try:
                dados_json = json.load(arquivo)
                collection_name = request.form['collection']
                collection = db[collection_name]
                
                if isinstance(dados_json, list):
                    collection.insert_many(dados_json)
                else:
                    collection.insert_one(dados_json)
                
                message = 'Arquivo importado com sucesso!'
            except Exception as e:
                message = f'Erro ao importar o arquivo: {e}'
        # Quando for um POST para consultar
        elif 'collection_select' in request.form:
            collection_name = request.form['collection_select']
            collection = db[collection_name]
            data = list(collection.find())  # Consultar todos os documentos na coleção

    return render_template('index.html', message=message, data=data)

if __name__ == '__main__':
    app.run(debug=True)
