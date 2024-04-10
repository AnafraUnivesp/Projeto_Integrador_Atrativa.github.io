# Anotações

Passo 01

Instalar o Python na máquina

* http://127.0.0.1:5000 : Ip local de desesenvolvimento + porta 
* Será mudada para http://localhost.5000
* Realizamos uma requisição através do localhost, porém não informamos a rota para retorno nas informações
* Ao verificar o log nos deparamos com 3 etapas de retorno do servidor we:
    * Método: GET (pesquisar metodos)
    * Rota: /
    * Código de Status de retorno: 404 ( pesquisar status codeweb) <!-- 202: requisão bem sucedida e o servidor retorno o que foi solicitado | 404: A rota solicitada não foi encontrada no servidor | 405: A rota existe, porém o método de requisão usado não é suportado por essa rota( GET,PUT e etc) | 500: Erro no servidor que impediu a requisição e gerou algum erro no backend -->


    * O cliente fez a requição da rota principal ( rota /), o backend encontrou essa rota e executou a função atrelada à rota e a função retornou uma resposta exibida no site. O site retornou o status 200


<!-- 

# main.py arquivo principal que irá rodar o script.

# Passo 01: Importando o Flask (Caso gere um erro, instalar via pip install)
# flask=Biblioteca   Flask=Classe principla quer irá chamar o flask

# Inicialização da Rota
from flask import Flask, url_for, render_template 

app = Flask(__name__) # indentificando e organizando recursos que irão receber o Flask

# Passo 02 - Faça um teste abrindo o terminal e execute o python main.py 

# Passo 03 - Definir rotas no Flask: sempre 
# Rotas ( estrutura básica de uma rota)

# @app.route('/') # /= rota principal e também podemos inserir os métodos, porém por padrão só é aceito o método GET
# def ola_mundo(): # função que recebe a requisição ( string, html, json)
#    return"Minha primeira estrutura de rota"  # mensagem de retorno da função


#Passo 05 - Podemos navegar entre as rotas do site
# url_for monta funções internas de acordo com a minha rota
@app.route("/")
def ola_atrativa():
    return render_template("index.html")

# Passo 04: Testando uma segunda rota com mais informações:x'x'
@app.route("/estoque") #lembra de informar a próxima rota
def pagina_estoque(): 

    return """
        <b> Projeto Integrador: </b> Testando nossa página de input de itens para estoque
        <a href ="https://anafraunivesp.github.io/website01.github.io/">.</a>

"""

# Finalizando a Rota: Sempre deve estar no final do código
# Responsável por executar o nosso servidor web
# executando
app.run(debug=True) 

-->

