# create_tables.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from database import engine, Base
from models.developer import Developer
from models.company import Company
from models.project import Project
from models.freebie import Freebie


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created!")

if __name__ == "__main__":
    create_tables()
