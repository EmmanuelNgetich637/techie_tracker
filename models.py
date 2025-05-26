from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class Developer(Base):
    __tablename__="developers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    years_of_experience = Column(Integer)

    freebies = relationship("Freebie", back_populates="developer")

    def __repr__(self):
        return f"<Developer(name={self.name}, specialty={self.specialty})>"
    
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)

    projects = relationship("Project", back_populates="company")
    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f"<Company(name={self.name}, location={self.location})>"

class Project(Base):
    __tablename__= "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="projects")

class Freebie(Base):
    __tablename__= "freebies"

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Float)
    developer_id = Column(Integer, ForeignKey("developers.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    developer = relationship("Developer", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")
