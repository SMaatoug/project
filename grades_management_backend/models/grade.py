from sqlalchemy import Column, Integer, ForeignKey, Float
from utils.database import Base

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey('students.id'), nullable=False)
    moduleId = Column(Integer, ForeignKey('modules.id'), nullable=False)
    labId = Column(Integer, ForeignKey('labs.id'))
    gradeValue = Column(Float, nullable=False)
