from flask import Blueprint, request, jsonify
from models.module import Module
from utils.database import db_session

module_routes = Blueprint('module', __name__)

@module_routes.route('/', methods=['POST'])
def create_module():
    data = request.get_json()
    new_module = Module(name=data['name'], semester=data['semester'], teacherId=data['teacherId'])
    db_session.add(new_module)
    db_session.commit()
    return jsonify({"message": "Module created successfully!"}), 201

@module_routes.route('/', methods=['GET'])
def get_all_modules():
    modules = Module.query.all()
    return jsonify([module.serialize for module in modules]), 200

@module_routes.route('/<int:module_id>', methods=['GET'])
def get_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        return jsonify({"message": "Module not found!"}), 404
    return jsonify(module.serialize), 200

@module_routes.route('/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        return jsonify({"message": "Module not found!"}), 404
    data = request.get_json()
    module.name = data['name']
    module.semester = data['semester']
    db_session.commit()
    return jsonify({"message": "Module updated successfully!"}), 200

@module_routes.route('/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        return jsonify({"message": "Module not found!"}), 404
    db_session.delete(module)
    db_session.commit()
    return jsonify({"message": "Module deleted successfully!"}), 200
