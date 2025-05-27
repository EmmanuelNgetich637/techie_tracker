from database import SessionLocal
from models.project import Project
from models.company import Company

def project_menu():
    session = SessionLocal()
    while True:
        print("\n--- Project Menu ---")
        print("1. View Projects")
        print("2. Add Project")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Back")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            projects = session.query(Project).all()
            if not projects:
                print("No projects found.")
            for project in projects:
                company_name = project.company.name if project.company else "None"
                print(f"ID: {project.id} | Name: {project.name} | Company: {company_name}")
        elif choice == "2":
            name = input("Project Name: ")
            # List companies to associate project with
            companies = session.query(Company).all()
            if not companies:
                print("No companies found. Please add a company first.")
                continue
            print("Select Company by ID:")
            for c in companies:
                print(f"{c.id}: {c.name}")
            company_id = input("Company ID: ")
            company = session.query(Company).get(company_id)
            if not company:
                print("Invalid company ID.")
                continue
            try:
                project = Project(name=name, company=company)
                session.add(project)
                session.commit()
                print("Project added.")
            except Exception as e:
                session.rollback()
                print("Error:", e)
        elif choice == "3":
            project_id = input("Enter Project ID to update: ")
            project = session.query(Project).get(project_id)
            if project:
                project.name = input(f"Name ({project.name}): ") or project.name
                # Optionally update company
                change_company = input("Change company? (y/n): ").lower()
                if change_company == "y":
                    companies = session.query(Company).all()
                    for c in companies:
                        print(f"{c.id}: {c.name}")
                    company_id = input("New Company ID: ")
                    company = session.query(Company).get(company_id)
                    if company:
                        project.company = company
                    else:
                        print("Invalid company ID. Skipping company update.")
                session.commit()
                print("Project updated.")
            else:
                print("Project not found.")
        elif choice == "4":
            project_id = input("Enter Project ID to delete: ")
            project = session.query(Project).get(project_id)
            if project:
                session.delete(project)
                session.commit()
                print("Project deleted.")
            else:
                print("Project not found.")
        elif choice == "5":
            session.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    project_menu()