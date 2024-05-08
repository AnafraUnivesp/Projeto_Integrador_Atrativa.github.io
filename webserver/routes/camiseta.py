from flask import Blueprint, render_template,request 
from database.models.camiseta import Camiseta


camiseta_route = Blueprint('camiseta', __name__)

@camiseta_route.route('/<string:item>', methods = ['GET'])
def lista_camiseta(item):
    camisetas = Camiseta.select().where(Camiseta.item==item)

    return render_template('lista_camiseta.html', camiseta=camisetas)

@camiseta_route.route('/', methods=['POST'])
def inserir_camiseta():
    """ Inserir os dados do estoque"""    

    data = request.json
    
    nova_camiseta = Camiseta.create(         
        item = data['item'],
        modelo = data['modelo'],  
        tipo = data['tipo'],   
        cor = data['cor'],  
        tamanho = data['tamanho'],  
        detalhe = data['detalhe'] 
    )
    
    return render_template('item_camiseta.html', camiseta=nova_camiseta)


@camiseta_route.route('/new')
def form_camiseta():
    """ Formulário para cadastrar um item de estoque"""
    return render_template('form_camiseta.html')


@camiseta_route.route('/<int:camiseta_id>')
def detalhe_camiseta(camiseta_id):
    """ Exibir detalhes do item de estoque"""

    camiseta = Camiseta.get_by_id(camiseta_id)
    
    return render_template('detalhe_camiseta.html', camiseta=camiseta)


@camiseta_route.route('/<int:camiseta_id>/edit')
def form_edit_camiseta(camiseta_id):
    """ Formulário para editar um item de estoque"""
    camiseta = Camiseta.get_by_id(camiseta_id)
    return render_template('form_camiseta.html', camiseta=camiseta)


@camiseta_route.route('/<int:camiseta_id>/update', methods=['PUT'])
def atualizar_camiseta(camiseta_id):
    """ Atualizar informações do item de estoque"""
    camiseta_editada = None

    #obter dados do formulário de edicao
    data = request.json

    camiseta_editada = Camiseta.get_by_id(camiseta_id)    
    camiseta_editada.item = data['item']
    camiseta_editada.modelo = data['modelo']  
    camiseta_editada.tipo = data['tipo']   
    camiseta_editada.cor = data['cor']
    camiseta_editada.tamanho = data['tamanho'] 
    camiseta_editada.detalhe = data['detalhe'] 
    camiseta_editada.save()        

    #editar o item 
    return render_template('item_camiseta.html', camiseta=camiseta_editada)             


@camiseta_route.route('/<int:camiseta_id>/delete', methods=['DELETE'])
def deletar_camiseta(camiseta_id):
    """ Deletar item de estoque"""
    camiseta = Camiseta.get_by_id(camiseta_id) 
    camiseta.delete_instance()
    return {'delete': 'ok'}

@camiseta_route.route('/<string:camiseta_item>', methods = ['GET'])
def buscar_por_item(camiseta_item):
    camisetas = Camiseta.select().where(Camiseta.item==camiseta_item)

    return render_template('lista_camiseta.html', camiseta=camisetas)


