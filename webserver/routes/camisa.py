from flask import Blueprint, render_template,request
from database.camisa import CAMISA   


camisa_route = Blueprint('camisa', __name__)

@camisa_route.route('/')
def lista_camisa():
    """ Listar o estoque"""
    return render_template('lista_camisa.html', camisa=CAMISA)

@camisa_route.route('/', methods=['POST'])
def inserir_camisa():
    """ Inserir os dados do estoque"""    
    data = request.json
    nova_camisa = {
        "id": len(CAMISA) + 1, 
        "item": data ['item'],
        "modelo": data ['modelo'],
        "tipo": data ['tipo'],
        "cor": data ['cor'],
        "tamanho": data ['tamanho'],
        "detalhe": data ['detalhe'],                
    }
    
    CAMISA.append(nova_camisa)
    return render_template('item_camisa.html', camisa=nova_camisa)


@camisa_route.route('/new')
def form_camisa():
    """ Formulário para cadastra um item de estoque"""
    return render_template('form_camisa.html')


@camisa_route.route('/<int:camisa_id>')
def detalhe_camisa(camisa_id):
    """ Exibir detalhes do item de estoque"""

    camisa = list(filter(lambda c: c['id'] == camisa_id, CAMISA)) [0]    
    
    return render_template('detalhe_camisa.html', camisa=camisa)


@camisa_route.route('/<int:camisa_id>/edit')
def form_edit_camisa(camisa_id):
    """ Formulário para editar um item de estoque"""
    camisa = None    
    for c in CAMISA:
        if c['id'] == camisa_id:
            camisa = c 
    return render_template('form_camisa.html', camisa=camisa)


@camisa_route.route('/<int:camisa_id>/update', methods=['PUT'])
def atualizar_camisa(camisa_id):
    """ Atualizar informações do item de estoque"""

    camisa_editada = None

    #obter dados do formulário de edicao
    data = request.json

    # obter item por id 
    for c in CAMISA:
        if  c['id'] == camisa_id:             
            c['item'] = data['item']  
            c['modelo'] = data['modelo']  
            c['tipo'] = data['tipo']   
            c['cor'] = data['cor']  
            c['tamanho'] = data['tamanho']  
            c['detalhe'] = data['detalhe']  

        camisa_editada = c                

    #editar o item 
    return render_template('item_camisa.html', camisa=camisa_editada)             


@camisa_route.route('/<int:camisa_id>/delete', methods=['DELETE'])
def deletar_camisa(camisa_id):
    """ Deletar item de estoque"""
    global CAMISA
    CAMISA = [ c for c in CAMISA if c ['id'] != camisa_id ]
    return {'delete': 'ok'}