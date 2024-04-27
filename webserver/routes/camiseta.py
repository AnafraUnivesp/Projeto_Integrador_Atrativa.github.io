from flask import Blueprint, render_template,request
from database.camiseta import CAMISETA   


camiseta_route = Blueprint('camiseta', __name__)

@camiseta_route.route('/')
def lista_camiseta():
    """ Listar o estoque"""
    return render_template('lista_camiseta.html', camiseta=CAMISETA)

@camiseta_route.route('/', methods=['POST'])
def inserir_camiseta():
    """ Inserir os dados do estoque"""    
    data = request.json
    nova_camiseta = {
        "id": len(CAMISETA) + 1, 
        "item": data ['item'],
        "modelo": data ['modelo'],
        "tipo": data ['tipo'],
        "marca": data ['marca'],
        "cor": data ['cor'],
        "tamanho": data ['tamanho'],
        "detalhe": data ['detalhe'],                
    }
    
    CAMISETA.append(nova_camiseta)
    return render_template('item_camiseta.html', camiseta=nova_camiseta)


@camiseta_route.route('/new')
def form_camiseta():
    """ Formulário para cadastra um item de estoque"""
    return render_template('form_camiseta.html')


@camiseta_route.route('/<int:camiseta_id>')
def detalhe_camiseta(camiseta_id):
    """ Exibir detalhes do item de estoque"""

    camiseta = list(filter(lambda c: c['id'] == camiseta_id, CAMISETA)) [0]    
    
    return render_template('detalhe_camiseta.html', camiseta=camiseta)


@camiseta_route.route('/<int:camiseta_id>/edit')
def form_edit_camiseta(camiseta_id):
    """ Formulário para editar um item de estoque"""
    camiseta = None    
    for c in CAMISETA:
        if c['id'] == camiseta_id:
            camiseta = c 
    return render_template('form_camiseta.html', camiseta=camiseta)


@camiseta_route.route('/<int:camiseta_id>/update', methods=['PUT'])
def atualizar_camiseta(camiseta_id):
    """ Atualizar informações do item de estoque"""

    camiseta_editada = None

    #obter dados do formulário de edicao
    data = request.json

    # obter item por id 
    for c in CAMISETA:
        if  c['id'] == camiseta_id:             
            c['item'] = data['item']  
            c['modelo'] = data['modelo']  
            c['tipo'] = data['tipo']   
            c['marca'] = data['marca'] 
            c['cor'] = data['cor']  
            c['tamanho'] = data['tamanho']  
            c['detalhe'] = data['detalhe']  

        camiseta_editada = c                

    #editar o item 
    return render_template('item_camiseta.html', camiseta=camiseta_editada)             


@camiseta_route.route('/<int:camiseta_id>/delete', methods=['DELETE'])
def deletar_camiseta(camiseta_id):
    """ Deletar item de estoque"""
    global CAMISETA
    CAMISETA = [ c for c in CAMISETA if c ['id'] != camiseta_id ]
    return {'delete': 'ok'}



