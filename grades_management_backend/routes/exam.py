from flask import Blueprint, request, jsonify
from models.exam import Exam
from utils.database import db_session

exam_routes = Blueprint('exam', __name__)

@exam_routes.route('/', methods=['POST'])
def create_exam():
    data = request.get_json()
    new_exam = Exam(moduleId=data['moduleId'], weight=data['weight'], gradeValue=data['gradeValue'])
    db_session.add(new_exam)
    db_session.commit()
    return jsonify({"message": "Exam created successfully!"}), 201

@exam_routes.route('/', methods=['GET'])
def get_all_exams():
    exams = Exam.query.all()
    return jsonify([exam.serialize for exam in exams]), 200

@exam_routes.route('/<int:module_id>', methods=['GET'])
def get_exam(module_id):
    exam = Exam.query.get(module_id)
    if not exam:
        return jsonify({"message": "Exam not found!"}), 404
    return jsonify(exam.serialize), 200

@exam_routes.route('/<int:module_id>', methods=['PUT'])
def update_exam(module_id):
    exam = Exam.query.get(module_id)
    if not exam:
        return jsonify({"message": "Exam not found!"}), 404
    data = request.get_json()
    exam.weight = data['weight']
    exam.gradeValue = data['gradeValue']
    db_session.commit()
    return jsonify({"message": "Exam updated successfully!"}), 200

@exam_routes.route('/<int:module_id>', methods=['DELETE'])
def delete_exam(module_id):
    exam = Exam.query.get(module_id)
    if not exam:
        return jsonify({"message": "Exam not found!"}), 404
    db_session.delete(exam)
    db_session.commit()
    return jsonify({"message": "Exam deleted successfully!"}), 200
