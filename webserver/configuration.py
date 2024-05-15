from routes.home import home_route
from routes.camiseta import camiseta_route
<<<<<<< HEAD
from routes.camisa import camisa_route
=======
>>>>>>> origin
from database.database import db
from database.models.camiseta import Camiseta

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route) 
    app.register_blueprint(camiseta_route, url_prefix='/camiseta') 
<<<<<<< HEAD
    app.register_blueprint(camisa_route, url_prefix='/camisa') 
=======
>>>>>>> origin

def configure_db():
    db.connect()
    db.create_tables([Camiseta])