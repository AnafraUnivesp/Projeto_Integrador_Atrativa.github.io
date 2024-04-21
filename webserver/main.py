
from flask import Flask
from routes.home import home_route
from routes.estoque import estoque_route 

app = Flask(__name__) 

app.register_blueprint(home_route) 
app.register_blueprint(estoque_route, url_prefix='/estoque') 

app.run(debug=True) 

