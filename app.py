from flask import Flask, jsonify

app = Flask(__name__)

lista = [
    {
        "id": u"1",
        "Plataforma": u"PC",
        "Nome": u"BFV",
        "Preco": u"250"
    },
    {
        "id": u"2",
        "Plataforma": u"PS4",
        "Nome": u"BFV",
        "Preco": u"250"
    },
    {
        "id": u"3",
        "Plataforma": u"XBOX ONE",
        "Nome": u"BFV",
        "Preco": u"250"
    }
]

@app.route('/jogos/api/v1/lista', methods=['GET'])
@app.route('/jogos/api/v1/lista/<int:id>', methods=['GET'])
def get_games(id=None):
    if id != None :
        return jsonify({'lista' : lista[(id-1)] })
    return jsonify({'lista': lista})

@app.route('/jogos/api/v1/lista/add/', methods=['POST'])
def add_games():
    if request.json:
        lista.append({
            "id": len(lista) + 1,
            "Plataforma": request.json[0]['Plataforma'],
            "Nome": request.json[0]['Nome'],
            "Preco": request.json[0]['Preco']
        })

@app.route('/jogos/api/v1/lista/alter/<int:id>', methods=['PUT'])
def put_games(id = None):
    if request.json and id != None:
        lista[(id-1)]['Plataforma'] = request.json[0]['Plataforma']
        lista[(id-1)]['Nome'] = request.json[0]['Nome']
        lista[(id-1)]['Preco'] = request.json[0]['Preco']
    return jsonify({'lista': lista})

@app.route('/jogos/api/v1/lista/del/<int:id>', methods=['DELETE'])
def del_games(id):
    return jsonify({'lista': lista})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'URL Não encontrada'}), 404)
                  
app.run(use_reloader=True)