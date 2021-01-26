from flask import send_from_directory
from __init__ import app

@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)