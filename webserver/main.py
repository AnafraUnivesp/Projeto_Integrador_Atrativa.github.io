# main.py arquivo principal que irá rodar o script.

# Passo 01: Importando o Flask (Caso gere um erro, instalar via pip install)
# flask=Biblioteca   Flask=Classe principla quer irá chamar o flask

# Inicialização da Rota
from flask import Flask, url_for 

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
    return f"<a href='{ url_for('pagina_estoque') }'>Gestão de Estoque Atrativa Store </a>" #função chamando a pagina_estoque


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

