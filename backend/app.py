import json
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import *

DB_FILE = "penncoursescompass.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db.init_app(app)

import re

UPLOAD_FOLDER = "/workspaces/PennCourseCompass/backend/uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return "Welcome to Penn Course Compass!"

@app.route('/api')
def home():
    return jsonify("Penn Course Compass is Alive!")

@app.route('/api/search/<course_code>', methods = ["GET"])
def search(course_code):
    # Make this query eager load the instructors and department as well, so we don't have to make more queries later
    # Use the selectinload parameter
    
    query = db.select(Course).options(
        db.selectinload(Course.instructors),
        db.selectinload(Course.dept) # type: ignore
    ).where(Course.number == course_code)

    result = db.session.execute(query).scalars().fetchmany(10)

    if not result:
        return {"error": f"Course({course_code}) not found"}, 401

    courses = [course.to_dict() for course in result]

    return jsonify(courses)


@app.route('/api/analyze', methods = ["POST"])
def analyze():
    return {}


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)