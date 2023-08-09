from utils.database import Base, engine
# Import all the models
from models.teacher import Teacher
from models.student import Student
from models.module import Module
from models.lab import Lab
from models.grade import Grade
from models.exam import Exam

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully!")
