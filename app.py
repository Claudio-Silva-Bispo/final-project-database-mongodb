from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://csspclaudio:clnzEcsY8xmMVXMr@cluster0.kfgkjua.mongodb.net/')
db = client['TestsDb']
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/importar', methods=['GET', 'POST'])
def importar():
    message = ""
    if request.method == 'POST':
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

    return render_template('importar.html', message=message)


@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    data = []
    if request.method == 'POST':
        collection_name = request.form['collection_select']
        collection = db[collection_name]
        data = list(collection.find())
    return render_template('consultar.html', data=data)


@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
    message = ""
    if request.method == 'POST':
        try:
            collection = request.form['collection_excluir']
            doc_id = request.form['id_excluir']
            db[collection].delete_one({'_id': ObjectId(doc_id)})
            message = "Documento excluído com sucesso!"
        except Exception as e:
            message = f"Erro ao excluir: {e}"

    return render_template('excluir.html', message=message)

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    doc = None
    collection_name = ""
    doc_id = ""
    message = ""

    if request.method == 'POST':
        # Fase 1: Buscar dados
        if 'buscar' in request.form:
            collection_name = request.form['collection']
            doc_id = request.form['id']
            try:
                doc = db[collection_name].find_one({'_id': ObjectId(doc_id)})
                if not doc:
                    message = "Documento não encontrado."
            except Exception as e:
                message = f"Erro ao buscar: {e}"

        # Fase 2: Salvar alterações
        elif 'salvar' in request.form:
            collection_name = request.form['collection']
            doc_id = request.form['id']
            novos_dados = request.form.to_dict()
            novos_dados.pop('collection')
            novos_dados.pop('id')
            novos_dados.pop('salvar')

            try:
                db[collection_name].update_one({'_id': ObjectId(doc_id)}, {'$set': novos_dados})
                message = "Documento atualizado com sucesso!"
            except Exception as e:
                message = f"Erro ao atualizar: {e}"

    return render_template('editar.html', doc=doc, collection=collection_name, id=doc_id, message=message)


if __name__ == '__main__':
    app.run(debug=True)
