from flask import Flask
from config import Config
from utils.database import db_session
from routes.auth import auth
from routes.module import module_routes
from routes.lab import lab_routes
from routes.student import student_routes
from routes.grade import grade_routes
from routes.exam import exam_routes
from flask_jwt_extended import JWTManager
from routes.upload import upload_routes
from routes.import_grades import import_grades_routes
from app import app
app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app) 

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(module_routes, url_prefix='/module')
app.register_blueprint(lab_routes, url_prefix='/lab')
app.register_blueprint(student_routes, url_prefix='/student')
app.register_blueprint(grade_routes, url_prefix='/grade')
app.register_blueprint(exam_routes, url_prefix='/exam')
app.register_blueprint(upload_routes)
app.register_blueprint(import_grades_routes)

if __name__ == '__main__':
    
    print(app.url_map)
    app.run(debug=True)
