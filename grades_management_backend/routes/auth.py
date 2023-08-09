from flask import Blueprint, request, jsonify, make_response
from models.teacher import Teacher
from utils.security import hash_password, verify_password
from utils.database import db_session
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = hash_password(data['password'])
    new_teacher = Teacher(firstName=data['firstName'], lastName=data['lastName'], email=data['email'], password=hashed_password)
    db_session.add(new_teacher)
    db_session.commit()
    return jsonify({"message": "Registration successful!"}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    teacher = Teacher.query.filter_by(email=data['email']).first()
    if teacher and verify_password(teacher.password, data['password']):
        access_token = create_access_token(identity=teacher.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials!"}), 401
