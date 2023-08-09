from flask import Blueprint, request, jsonify
from models.grade import Grade
from utils.database import db_session

grade_routes = Blueprint('grade', __name__)

@grade_routes.route('/', methods=['POST'])
def create_grade():
    data = request.get_json()
    new_grade = Grade(studentId=data['studentId'], moduleId=data['moduleId'], labId=data['labId'], gradeValue=data['gradeValue'])
    db_session.add(new_grade)
    db_session.commit()
    return jsonify({"message": "Grade created successfully!"}), 201

@grade_routes.route('/', methods=['GET'])
def get_all_grades():
    grades = Grade.query.all()
    return jsonify([grade.serialize for grade in grades]), 200

@grade_routes.route('/<int:grade_id>', methods=['GET'])
def get_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found!"}), 404
    return jsonify(grade.serialize), 200

@grade_routes.route('/<int:grade_id>', methods=['PUT'])
def update_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found!"}), 404
    data = request.get_json()
    grade.gradeValue = data['gradeValue']
    db_session.commit()
    return jsonify({"message": "Grade updated successfully!"}), 200

@grade_routes.route('/<int:grade_id>', methods=['DELETE'])
def delete_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found!"}), 404
    db_session.delete(grade)
    db_session.commit()
    return jsonify({"message": "Grade deleted successfully!"}), 200
