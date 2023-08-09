from flask import Blueprint, request, jsonify
from models.student import Student
from utils.database import db_session

student_routes = Blueprint('student', __name__)

@student_routes.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(registrationNumber=data['registrationNumber'], firstName=data['firstName'], lastName=data['lastName'], email=data['email'])
    db_session.add(new_student)
    db_session.commit()
    return jsonify({"message": "Student created successfully!"}), 201

@student_routes.route('/', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return jsonify([student.serialize for student in students]), 200

@student_routes.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found!"}), 404
    return jsonify(student.serialize), 200

@student_routes.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found!"}), 404
    data = request.get_json()
    student.firstName = data['firstName']
    student.lastName = data['lastName']
    student.email = data['email']
    db_session.commit()
    return jsonify({"message": "Student updated successfully!"}), 200

@student_routes.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found!"}), 404
    db_session.delete(student)
    db_session.commit()
    return jsonify({"message": "Student deleted successfully!"}), 200
