#!/bin/bash

# Create main project directory
mkdir grades_management_backend

# Navigate to project directory
cd grades_management_backend

# Create necessary directories
mkdir models routes utils

# Create necessary files
touch app.py config.py requirements.txt
touch models/__init__.py models/teacher.py models/student.py models/module.py models/lab.py models/grade.py models/exam.py
touch routes/__init__.py routes/auth.py routes/module.py routes/lab.py routes/student.py routes/grade.py
touch utils/__init__.py utils/database.py utils/security.py

# Print completion message
echo "Backend directory and file structure set up successfully!"