from flask import Blueprint, render_template
from database.estoque import ESTOQUE

estoque_route = Blueprint('estoque', __name__)

@estoque_route.route('/')
def lista_estoque():
    """ Listar o estoque"""
    return render_template('lista_estoque.html', estoque=ESTOQUE)


@estoque_route.route('/', methods=['POST'])
def inserir_estoque():
    """ Inserir os dados do estoque"""
    pass


@estoque_route.route('/new')
def form_estoque():
    """ Formulário para cadastra um item de estoque"""
    return render_template('form_estoque.html')


@estoque_route.route('/<int:estoque_id>')
def detalhe_estoque(estoque_id):
    """ Exibir detalhes do item de estoque"""
    return render_template('detalhe_estoque.html')


@estoque_route.route('/<int:estoque_id>/edit')
def form_edit_estoque(estoque_id):
    """ Formulário para editar um item de estoque"""
    return render_template('form_edit_estoque.html')


@estoque_route.route('/<int:estoque_id>/update', methods=['PUT'])
def atualizar_estoque(estoque_id):
    """ Atualizar informações do item de estoque"""
    pass


@estoque_route.route('/<int:estoque_id>/delete', methods=['DELETE'])
def deletar_estoque(estoque_id):
    """ Deletar item de estoque"""
    pass
