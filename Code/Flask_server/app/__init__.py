# Import flask and template operators
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable
from app.location.controllers import mod_loc

# Register blueprint(s)
app.register_blueprint(mod_loc)

# Build the database:
db.create_all()


# Setup the routes:
@app.route('/')


@app.route('/home')
def HOME():
    """Introduction.html

     Redirects to the homepage

    """
    return render_template('index.html')