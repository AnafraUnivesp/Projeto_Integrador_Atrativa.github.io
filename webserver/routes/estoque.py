from flask import Blueprint, render_template, request
from database.estoque import ESTOQUE

estoque_route = Blueprint('estoque', __name__)

"""
Rotas de Estoque
-/estoque/ (GET) - Listar os item camisa.
-/estoque/new (GET) - Renderiza um formulário para registrar um item camisa.
-/estoque/ (POST) - Inserir o item camisa no servidor.
-/estoque/<id> (GET) - Obter dados do item camisa.
-/estoque/<id>/edit (GET) - Renderizar um formulário para editar uma camisa.
-/estoque/<id>update (PUT) - Atualizar os dados do item camisa. 
-/estoque/<id>delete (DELETE) - Deleta o registro do item camisa.

"""

# rota 01 - Listando o item camisa
@estoque_route.route('/')
def lista_camisas():      # teremos que listar nossas peças de roupas, então criamos uma função lista
    """ Listar Clientes"""
    return render_template('lista_camisas.html', estoque=ESTOQUE)


# rota 02 - Inserindo o item camisa
@estoque_route.route('/', methods=['POST']) # Para criar usuário não tenho id
def inserir_camisas():    
    """ Inserir itens no banco de dados """ 

    data = request.json

    novo_item_estoque = {

        "id": len(ESTOQUE) + 1,
        "Camisas": data['Camisas'],
        "Modelo": data['Modelo'],
        "Marca": data['Marca'],
        "Tamanho": data['Tamanho'],            
        "Detalhes": data['Detalhes'], 
    }
    
    ESTOQUE.append(novo_item_estoque)

    return render_template('novo_item_estoque.html', estoque=novo_item_estoque)

# rota 03 - Inserindo o item camisa
@estoque_route.route('/new') # Não foi mecionado o get, pois por padrão a rota é GET
def form_cadas_camisas(): 
    """ Formulário para criar cadastrar um novo item """
    return render_template('form_cadas_camisas.html')

# rota 04 - Obtendo detalhes
@estoque_route.route('/<int:camisa_id>') # dinâmico: tipo do parâmetro
def obter_camisas(camisa_id): 
     """ Exibir detalhes do item  """
     return render_template('obter_camisas.html')

# rota 05 - Editando dados do item
@estoque_route.route('/<int:camisa_id>/edit') # dinâmico: tipo do parâmetro
def form_editar_camisas(camisa_id): 
     """ Formulário para editar os dados de um item  """
     return render_template('form_editar_camisas.html')

# rota 06 - Atualizando infos do item
@estoque_route.route('/<int:camisa_id>/update', methods=['PUT']) # Para criar usuário não tenho id
def atualizar_camisas(camisa_id):    
    """ Atualizar informações do item """ 
    pass


# rota 07 - Atualizando infos do item
@estoque_route.route('/<int:camisa_id>/delete', methods=['DELETE']) # Para criar usuário não tenho id
def deletar_camisas(camisa_id):    
    """ Deletando informações do item """ 
    pass