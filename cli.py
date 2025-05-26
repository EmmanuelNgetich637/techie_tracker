from database import SessionLocal
from models import Developer, Company
import sys

def menu():
    print("\n--- Techie Tracker CLI ---")
    print("1. View all developers")
    print("2. View all companies")
    print("3. Add a developer")
    print("4. Add a company")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice 

def view_developers(session):
    developers = session.query(Developer).all()
    print("\n--- Developers ---")
    if not developers:
        print("No developers found.")
    for dev in developers:
        print(f"ID: {dev.id} | Name: {dev.name} | Specialty: {dev.specialty}")

def view_companies(session):
    companies = session.query(Company).all()
    print("\n--- Companies ---")
    if not companies:
        print("No companies found.")
    for company in companies:
        print(f"ID: {company.id} | Name: {company.name} | Location: {company.location}")
    
def add_developer(session):
    print("\n--- Add Developer ---")
    name = input("Name: ")
    specialty = input("Specialty: ")
    experience = input("Year of Experience: ")

    try:
        dev = Developer(name=name, specialty=specialty, year_of_experience=int(experience))
        session.add(dev)
        session.commit()
        print("✅ Developer added successfully.")
    except Exception as e:
        session.rollback()
        print("❌ Error:", e)

def add_company(session):
    print("\n--- Add Company ---")
    name = input("Company Name: ")
    location = input("Location: ")

    try:
        company = Company(name=name, location=location)
        session.add(company)
        session.commit()
        print("✅ Company added successfully.")
    except Exception as e:
        session.rollback()
        print("❌ Error:", e)

def main():
    session = SessionLocal()
    while True:
        choice = menu()
        if choice == "1":
            view_developers(session)
        elif choice == "2":
            view_companies(session)
        elif choice == "3":
            add_developer(session)
        elif choice == "4":
            add_company(session)
        elif choice == "5":
            print("Existing... 👋")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
