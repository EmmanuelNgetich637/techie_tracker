from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Freebie(Base):
    __tablename__ = "freebies"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="freebies")
    