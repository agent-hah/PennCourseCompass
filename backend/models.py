from extensions import db

# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/


from sqlalchemy import String, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from werkzeug.security import generate_password_hash, check_password_hash

course_instructor_association = Table(
    "department_course_association",
    db.metadata,
    db.Column("instructor_id", ForeignKey("instructors.id"), primary_key = True),
    db.Column("course_id", ForeignKey("courses.id"), primary_key = True)
)

class Course(db.Model):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(db.Integer, primary_key= True)

    dept_id: Mapped[int] = mapped_column(db.Integer, ForeignKey("departments.id"), nullable= False) 

    name: Mapped[str] = mapped_column(db.String(12), unique = True)

    number: Mapped[int] = mapped_column(db.Integer, unique = True)

    description: Mapped[str] = mapped_column(db.String)

    instructors = db.relationship(
        "Instructor",
        secondary = course_instructor_association, 
        back_populates = "courses",
        lazy = True
        )

class Department(db.Model):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)

    name: Mapped[str] = mapped_column(db.String(5), unique = True)
    
    courses = db.relationship("Course", backref = "dept", lazy = 'dynamic')

class Instructor(db.Model):
    __tablename__ = "instructors"

    id: Mapped[int] = mapped_column(db.Integer, primary_key= True)

    name: Mapped[str] = mapped_column(db.String)

    courses = db.relationship(
        "Course",
        secondary = course_instructor_association,
        back_populates = "instructors",
        lazy = True
        )
    