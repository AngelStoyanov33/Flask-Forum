from sqlalchemy.sql import func
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask.app import Flask
import appsettings
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
#db = SQLAlchemy(app)

    
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.secret_key = appsettings.secretKey
db = SQLAlchemy(app)

from routes import register, login, index, home