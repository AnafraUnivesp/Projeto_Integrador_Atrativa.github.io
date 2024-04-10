# Inicialização da Rota
from flask import Flask, url_for, render_template 

app = Flask(__name__) 

#rota 01
@app.route("/")
def ola_atrativa():
    titulo ="Gestão de Estoque"
    clote = [
        {"partnumberl": "L001", "disponivel": False },
        {"partnumberl": "L002", "disponivel": True },
        {"partnumberl": "L003", "disponivel": False },
    ]

    cpeca = [
        {"partnumberp": "P001", "disponivel": True },
        {"partnumberp": "P002", "disponivel": False },
        {"partnumberp": "P003", "disponivel": True },
    ]
    
    tamanho = [    
        {"partnumberp": "P001", "numeracao": "GG", "disponivel": True },
        {"partnumberp": "P002", "numeracao": "P", "disponivel": False },
        {"partnumberp": "P003", "numeracao": "M", "disponivel": True },
    ]
    return render_template("index.html", titulo=titulo,clote=clote,cpeca=cpeca,tamanho=tamanho) # variavel de contexto ( html) + variavel de funcao (backend)

#rota 02
@app.route("/estoque") 
def pagina_estoque(): 

    return """
        <b> Projeto Integrador: </b> Testando nossa página de input de itens para estoque
        <a href ="https://anafraunivesp.github.io/website01.github.io/">.</a>

"""

# finalizando a execução
app.run(debug=True) 

