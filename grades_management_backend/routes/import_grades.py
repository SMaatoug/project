from flask import Blueprint, jsonify, request
import pandas as pd
from models.student import Student
from models.grade import Grade
from models.lab import Lab
from models.exam import Exam
from utils.database import session

import_grades_routes = Blueprint('import_grades_routes', __name__)

@import_grades_routes.route('/import_grades/<module_id>', methods=['POST'])
def import_grades(module_id):
    filename = request.json.get('filename')
    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    try:
        if filename.endswith('.csv'):
            data = pd.read_csv(filename)
        elif filename.endswith('.xlsx'):
            data = pd.read_excel(filename)

        # Extracting module name from a column
        module_name = data.columns[4].split(" - ")[0]

        errors = []
        success_count = 0
        for index, row in data.iterrows():
            student = session.query(Student).filter_by(registration_number=row['Registration Number']).first()
            if student:
                # Loop through labs
                for col in data.columns[4:-1]:  # Excluding the last column which is for the exam
                    lab_name = col.split(" - ")[1]
                    lab = Lab(student_id=student.id, module_id=module_id, name=lab_name, score=row[col])
                    session.add(lab)

                # Handle exam
                exam_score = row[data.columns[-1]]
                exam = Exam(student_id=student.id, module_id=module_id, score=exam_score)
                session.add(exam)

                success_count += 1
            else:
                errors.append(f"Student with registration number {row['Registration Number']} not found.")

        session.commit()
        return jsonify({"message": f"Successfully imported {success_count} grades.", "errors": errors}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
