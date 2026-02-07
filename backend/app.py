import json
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

DB_FILE = "penncoursescompass.db"

from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

import re

UPLOAD_FOLDER = "/workspaces/PennCourseCompass/backend/uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api')
def home():
    return "Penn Course Compass is Alive!"

@app.route('/api/search/<course_code>', methods = ["GET"])
def search(course_code):
    return {}
    
@app.route('/api/analyze', methods = ["POST"])
def analyze():
    return {}


if __name__ == '__main__':
    # We use 0.0.0.0 so the container exposes it to your machine
    app.run(host='0.0.0.0', port=5000, debug=True)