from sqlalchemy import Column, Integer, String, ForeignKey, Float
from utils.database import Base

class Lab(Base):
    __tablename__ = 'labs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    moduleId = Column(Integer, ForeignKey('modules.id'), nullable=False)
    weight = Column(Float, nullable=False)
