from routes.home import home_route
from routes.camiseta import camiseta_route
from database.database import db
from database.models.camiseta import Camiseta

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route) 
    app.register_blueprint(camiseta_route, url_prefix='/camiseta') 

def configure_db():
    db.connect()
    db.create_tables([Camiseta])