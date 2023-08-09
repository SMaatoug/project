from flask import Blueprint, request, jsonify
from models.lab import Lab
from utils.database import db_session

lab_routes = Blueprint('lab', __name__)

@lab_routes.route('/', methods=['POST'])
def create_lab():
    data = request.get_json()
    new_lab = Lab(name=data['name'], moduleId=data['moduleId'], weight=data['weight'])
    db_session.add(new_lab)
    db_session.commit()
    return jsonify({"message": "Lab created successfully!"}), 201

@lab_routes.route('/', methods=['GET'])
def get_all_labs():
    labs = Lab.query.all()
    return jsonify([lab.serialize for lab in labs]), 200

@lab_routes.route('/<int:lab_id>', methods=['GET'])
def get_lab(lab_id):
    lab = Lab.query.get(lab_id)
    if not lab:
        return jsonify({"message": "Lab not found!"}), 404
    return jsonify(lab.serialize), 200

@lab_routes.route('/<int:lab_id>', methods=['PUT'])
def update_lab(lab_id):
    lab = Lab.query.get(lab_id)
    if not lab:
        return jsonify({"message": "Lab not found!"}), 404
    data = request.get_json()
    lab.name = data['name']
    lab.weight = data['weight']
    db_session.commit()
    return jsonify({"message": "Lab updated successfully!"}), 200

@lab_routes.route('/<int:lab_id>', methods=['DELETE'])
def delete_lab(lab_id):
    lab = Lab.query.get(lab_id)
    if not lab:
        return jsonify({"message": "Lab not found!"}), 404
    db_session.delete(lab)
    db_session.commit()
    return jsonify({"message": "Lab deleted successfully!"}), 200
