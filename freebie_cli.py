from database import SessionLocal
from models.freebie import Freebie
from models.project import Project

def freebie_menu():
    session = SessionLocal()
    while True:
        print("\n--- Freebie Menu ---")
        print("1. View Freebies")
        print("2. Add Freebie")
        print("3. Update Freebie")
        print("4. Delete Freebie")
        print("5. Back")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            freebies = session.query(Freebie).all()
            if not freebies:
                print("No freebies found.")
            for freebie in freebies:
                project_name = freebie.project.name if freebie.project else "None"
                print(f"ID: {freebie.id} | Item: {freebie.item_name} | Project: {project_name}")
        elif choice == "2":
            item_name = input("Freebie Item Name: ")
            projects = session.query(Project).all()
            if not projects:
                print("No projects found. Please add a project first.")
                continue
            print("Select Project by ID:")
            for p in projects:
                print(f"{p.id}: {p.name}")
            project_id = input("Project ID: ")
            project = session.query(Project).get(project_id)
            if not project:
                print("Invalid project ID.")
                continue
            try:
                freebie = Freebie(item_name=item_name, project=project)
                session.add(freebie)
                session.commit()
                print("Freebie added.")
            except Exception as e:
                session.rollback()
                print("Error:", e)
        elif choice == "3":
            freebie_id = input("Enter Freebie ID to update: ")
            freebie = session.query(Freebie).get(freebie_id)
            if freebie:
                freebie.item_name = input(f"Item Name ({freebie.item_name}): ") or freebie.item_name
                change_project = input("Change project? (y/n): ").lower()
                if change_project == "y":
                    projects = session.query(Project).all()
                    for p in projects:
                        print(f"{p.id}: {p.name}")
                    project_id = input("New Project ID: ")
                    project = session.query(Project).get(project_id)
                    if project:
                        freebie.project = project
                    else:
                        print("Invalid project ID. Skipping project update.")
                session.commit()
                print("Freebie updated.")
            else:
                print("Freebie not found.")
        elif choice == "4":
            freebie_id = input("Enter Freebie ID to delete: ")
            freebie = session.query(Freebie).get(freebie_id)
            if freebie:
                session.delete(freebie)
                session.commit()
                print("Freebie deleted.")
            else:
                print("Freebie not found.")
        elif choice == "5":
            session.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    freebie_menu()