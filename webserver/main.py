
from flask import Flask
from routes.home import home_route # importando a rota e a variável da homeroutes
from routes.estoque import estoque_route # importando a rota estoque

app = Flask(__name__) 

app.register_blueprint(home_route)
app.register_blueprint(estoque_route, url_prefix='/estoque') # lembrar do prefixo /estoque/ 

app.run(debug=True) 

