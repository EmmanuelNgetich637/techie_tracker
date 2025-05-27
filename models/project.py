from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="projects")
    freebies = relationship("Freebie", back_populates="project")

