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

    instructors: Mapped[List["Instructor"]] = relationship(
        "Instructor",
        secondary = course_instructor_association, 
        back_populates = "courses",
        lazy = True
        )
    
    def to_dict(self):
        return {
            "dept_name": self.dept.name, #type: ignore
            "name": self.name,
            "course_code": self.number,
            "description": self.description,
            "instructors": [instructor.name for instructor in self.instructors]
        }

class Department(db.Model):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)

    name: Mapped[str] = mapped_column(db.String(5), unique = True)
    
    courses: Mapped[List["Course"]] = relationship("Course", backref = "dept", lazy = 'dynamic')

    def to_dict(self):
        return {
            "name": self.name,
            "courses": [(f'{course.dept.name}{course.number}', course.name) for course in self.courses] # type: ignore
        }

class Instructor(db.Model):
    __tablename__ = "instructors"

    id: Mapped[int] = mapped_column(db.Integer, primary_key= True)

    name: Mapped[str] = mapped_column(db.String)

    courses: Mapped[List["Course"]] = relationship(
        "Course",
        secondary = course_instructor_association,
        back_populates = "instructors",
        lazy = True
        )
    
    def to_dict(self):
        return {
            "name": self.name,
            "courses": [(f'{course.dept.name}{course.number}', course.name) for course in self.courses] # type: ignore
        }