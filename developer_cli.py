from database import SessionLocal
from models.developer import Developer

def developer_menu():
    session = SessionLocal()
    while True:
        print("\n--- Developer Menu ---")
        print("1. View Developers")
        print("2. Add Developer")
        print("3. Update Developer")
        print("4. Delete Developer")
        print("5. Back")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            developers = session.query(Developer).all()
            if not developers:
                print("No developers found.")
            for dev in developers:
                print(f"ID: {dev.id} | Name: {dev.name} | Specialty: {dev.specialty} | Experience: {dev.year_of_experience}")
        elif choice == "2":
            name = input("Name: ")
            specialty = input("Specialty: ")
            experience = input("Years of experience: ")
            try:
                dev = Developer(name=name, specialty=specialty, year_of_experience=int(experience))
                session.add(dev)
                session.commit()
                print("Developer added.")
            except Exception as e:
                session.rollback()
                print("Error:", e)
        elif choice == "3":
            dev_id = input("Enter Developer ID to update: ")
            dev = session.query(Developer).get(dev_id)
            if dev:
                dev.name = input(f"Name ({dev.name}): ") or dev.name
                dev.specialty = input(f"Specialty ({dev.specialty}): ") or dev.specialty
                exp = input(f"Years of experience ({dev.year_of_experience}): ")
                if exp:
                    dev.year_of_experience = int(exp)
                session.commit()
                print("Developer updated.")
            else:
                print("Developer not found.")
        elif choice == "4":
            dev_id = input("Enter Developer ID to delete: ")
            dev = session.query(Developer).get(dev_id)
            if dev:
                session.delete(dev)
                session.commit()
                print("Developer deleted.")
            else:
                print("Developer not found.")
        elif choice == "5":
            session.close()
            break
        else:
            print("Invalid choice. Try again.")
