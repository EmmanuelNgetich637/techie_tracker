from database import SessionLocal
from models.company import Company

def company_menu():
    session = SessionLocal()
    while True:
        print("\n--- Company Menu ---")
        print("1. View Companies")
        print("2. Add Company")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Back")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            companies = session.query(Company).all()
            if not companies:
                print("No companies found.")
            for company in companies:
                print(f"ID: {company.id} | Name: {company.name} | Location: {company.location}")
        elif choice == "2":
            name = input("Company Name: ")
            location = input("Location: ")
            try:
                company = Company(name=name, location=location)
                session.add(company)
                session.commit()
                print("Company added.")
            except Exception as e:
                session.rollback()
                print("Error:", e)
        elif choice == "3":
            company_id = input("Enter Company ID to update: ")
            company = session.query(Company).get(company_id)
            if company:
                company.name = input(f"Name ({company.name}): ") or company.name
                company.location = input(f"Location ({company.location}): ") or company.location
                session.commit()
                print("Company updated.")
            else:
                print("Company not found.")
        elif choice == "4":
            company_id = input("Enter Company ID to delete: ")
            company = session.query(Company).get(company_id)
            if company:
                session.delete(company)
                session.commit()
                print("Company deleted.")
            else:
                print("Company not found.")
        elif choice == "5":
            session.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    company_menu()
