from sqlalchemy import Column, Integer, ForeignKey, Float
from utils.database import Base

class Exam(Base):
    __tablename__ = 'exams'

    moduleId = Column(Integer, ForeignKey('modules.id'), primary_key=True)
    weight = Column(Float, nullable=False)
    gradeValue = Column(Float)
