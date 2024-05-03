
from flask import Flask
from routes.home import home_route
from routes.camiseta import camiseta_route
from routes.camisa import camisa_route


app = Flask(__name__) 

app.register_blueprint(home_route) 
app.register_blueprint(camiseta_route, url_prefix='/camiseta') 
app.register_blueprint(camisa_route, url_prefix='/camisa') 

app.run(debug=True) 

