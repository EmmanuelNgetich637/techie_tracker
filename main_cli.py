from company_cli import company_menu
from project_cli import project_menu
from freebie_cli import freebie_menu
from developer_cli import developer_menu

def main_menu():
    while True:
        print("\n===== Techie Tracker Main Menu =====")
        print("1. Manage Companies")
        print("2. Manage Projects")
        print("3. Manage Freebies")
        print("4. Manage Developers")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            company_menu()
        elif choice == "2":
            project_menu()
        elif choice == "3":
            freebie_menu()
        elif choice == "4":
            developer_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()