
from flask import Flask
from configuration import configure_all



app = Flask(__name__) 

configure_all(app)
<<<<<<< HEAD

=======
>>>>>>> origin


app.run(debug=True) 