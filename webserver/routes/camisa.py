from flask import Blueprint, render_template
from database.camisa import CAMISA   


camisa_route = Blueprint('camisa', __name__)

@camisa_route.route('/')
def lista_camisa():
    """ Listar o estoque"""
    return render_template('lista_camisa.html', camisa=CAMISA)

@camisa_route.route('/', methods=['POST'])
def inserir_camisa():
    """ Inserir os dados do estoque"""
    pass


@camisa_route.route('/new')
def form_camisa():
    """ Formulário para cadastra um item de estoque"""
    return render_template('form_camisa.html')


@camisa_route.route('/<int:camisa_id>')
def detalhe_camisa(camisai_d):
    """ Exibir detalhes do item de estoque"""
    return render_template('detalhe_camisa.html')


@camisa_route.route('/<int:camisa_id>/edit')
def form_edit_camisa(camisa_id):
    """ Formulário para editar um item de estoque"""
    return render_template('form_edit_camisa.html')


@camisa_route.route('/<int:camisa_id>/update', methods=['PUT'])
def atualizar_camisa(camisa_id):
    """ Atualizar informações do item de estoque"""
    pass


@camisa_route.route('/<int:camisa_id>/delete', methods=['DELETE'])
def deletar_camisa(camisa_id):
    """ Deletar item de estoque"""
    pass
