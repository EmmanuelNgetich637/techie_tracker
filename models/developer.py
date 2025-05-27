from sqlalchemy import Column, Integer, String
from database import Base

class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    year_of_experience = Column(Integer)
    