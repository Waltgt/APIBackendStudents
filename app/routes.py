from flask import Blueprint, request
from .models import db, Students, Careers
from .schemas import (student_schema, students_schema, career_schema, careers_schema)

students_bp = Blueprint('students', __name__, url_prefix='/students')
careers_bp = Blueprint('careers', __name__, url_prefix='/careers')

@careers_bp.route('/', methods=['GET'])
def get_careers():
    careers = Careers.query.all()
    return careers_schema.dump(Careers.query.all()), 200

@students_bp.route('/', methods=['POST'])
def add_student():
    new_student = student_schema.load(request.json)
    db.session.add(new_student)
    db.session.commit()
    return student_schema.dump(new_student), 201

@students_bp.route('/', methods=['GET'])
def get_students():
    return students_schema.dump(Students.query.all()), 200

@students_bp.route("/", methods=["GET"])
def get_students():
    students = Students.query.all()
    return students_schema.dump(students), 200


@students_bp.route("/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Students.query.get_or_404(student_id)
    return student_schema.dump(student), 200


@students_bp.route("/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Students.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return "", 204


@students_bp.route("/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = Students.query.get_or_404(student_id)
    student_schema.load(request.json,instance=student,partial=True)
    db.session.commit()
    return student_schema.dump(student), 200

