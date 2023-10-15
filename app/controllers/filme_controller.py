from flask import jsonify
from app import app
from app.services import filme_service

filme_service.criar_tabela()
filme_service.importar_dados()

@app.route('/dados')
def obter_dados():
    dados = filme_service.mostrar_dados()
    return jsonify(dados)

@app.route('/intervalo_premios')
def obter_intervalo_premios():
    resultado_formatado = filme_service.obter_maior_intervalo_e_premio_mais_rapido()
    return jsonify(resultado_formatado)
