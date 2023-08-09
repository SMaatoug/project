from sqlalchemy import Column, Integer, String, ForeignKey
from utils.database import Base

class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    teacherId = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'semester': self.semester,
            'teacherId': self.teacherId
        }