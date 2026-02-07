import os

import json

from app import app, db, DB_FILE

from models import *


def load_data():
    # We are going to read the JSON file first through file IO
    try:
        with open('mock_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: mock_data.json file not found")
        return
    
    for entry in data:
        # Create the department if it doesn't exist
        department = db.session.execute(db.select(Department).where(Department.name == entry['dept'])).scalar_one_or_none()

        if not department:
            department = Department(
                name = entry['dept']
            )
            db.session.add(department)

        instructor_list = []
        for person in entry["instructors"]:
            instructor = db.session.execute(db.select(Instructor).where(Instructor.name == person)).scalar_one_or_none()
            
            if not instructor:
                instructor = Instructor(
                    name = person
                )
                db.session.add(instructor)
            instructor_list.append(instructor)
        

        # Create a new Course object
        course = Course(
            dept_id=department.id,
            name=entry['title'],
            number=entry['number'],
            description=entry['description'],
            instructors = instructor_list
        )

        department.courses.append(course)
        db.session.add(course)
        try:
            db.session.commit()
        except Exception as e:
            print(f"Error committing to database: {e}")
            db.session.rollback()


# No need to modify the below code.
if __name__ == "__main__":
    # Delete any existing database before bootstrapping a new one.
    LOCAL_DB_FILE = "instance/" + DB_FILE
    if os.path.exists(LOCAL_DB_FILE):
        os.remove(LOCAL_DB_FILE)

    with app.app_context():
        db.create_all()
        load_data()
