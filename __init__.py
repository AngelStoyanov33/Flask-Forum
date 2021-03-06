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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['UPLOAD_FOLDER'] = appsettings.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = appsettings.secret_key
db = SQLAlchemy(app)

from routes import register, login, index, home, topic, thread, profile, process, search, reply, view_thread, process_image, get_upload