from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/excluir', methods=['POST'])
def excluir_por_formulario():
    try:
        collection = request.form['collection_excluir']
        doc_id = request.form['id_excluir']
        db[collection].delete_one({'_id': ObjectId(doc_id)})
        message = "Documento excluído com sucesso!"
    except Exception as e:
        message = f"Erro ao excluir: {e}"
    
    # Retornar para a página inicial com a mensagem
    return render_template('index.html', message=message, data=[])

@app.route('/editar/<collection>/<id>', methods=['GET', 'POST'])
def editar_documento(collection, id):
    doc = db[collection].find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
        novos_dados = request.form.to_dict()
        try:
            db[collection].update_one({'_id': ObjectId(id)}, {'$set': novos_dados})
            return redirect(url_for('index'))
        except Exception as e:
            return f"Erro ao atualizar: {e}"

    return render_template('editar.html', doc=doc, collection=collection)

if __name__ == '__main__':
    app.run(debug=True)
